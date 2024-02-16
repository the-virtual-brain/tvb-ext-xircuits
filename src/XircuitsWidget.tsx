import { ReactWidget } from '@jupyterlab/apputils';
import { ILabShell, JupyterFrontEnd } from '@jupyterlab/application';
import { Signal } from '@lumino/signaling';
import { Context } from '@jupyterlab/docregistry';
import { BodyWidget } from './components/XircuitsBodyWidget';
import React from 'react';
import { ServiceManager } from '@jupyterlab/services';
import { XircuitsApplication } from './components/XircuitsApp';
import {requestAPI} from "./server/handler";
import {CustomNodeModel} from "./components/CustomNodeModel";
import {DefaultLinkModel, NodeModel} from "@projectstorm/react-diagrams";
import {PortModel} from "@projectstorm/react-diagrams-core";

/**
 * DocumentWidget: widget that represents the view or editor for a file type.
 */
export class XircuitsPanel extends ReactWidget {
  app: JupyterFrontEnd;
  shell: ILabShell;
  commands: any;
  context: Context;
  xircuitsApp: XircuitsApplication;
  serviceManager: ServiceManager;
  fetchComponentsSignal: Signal<this,any>;
  saveXircuitSignal: Signal<this, any>;
  compileXircuitSignal: Signal<this, any>;
  runXircuitSignal: Signal<this, any>;
  runTypeXircuitSignal: Signal<this, any>;
  lockNodeSignal: Signal<this, any>;
  reloadAllNodesSignal: Signal<this, any>;
  toggleAllLinkAnimationSignal: Signal<this, any>;

  // Add mousePosition state
  mousePosition = { x: 0, y: 0 };

  constructor(options: any) {
    super();
    this.app = options.app;
    this.shell = options.shell;
    this.commands = options.commands;
    this.context = options.context;
    this.serviceManager = options.serviceManager;
    this.fetchComponentsSignal = options.fetchComponentsSignal;
    this.saveXircuitSignal = options.saveXircuitSignal;
    this.compileXircuitSignal = options.compileXircuitSignal;
    this.runXircuitSignal = options.runXircuitSignal;
    this.runTypeXircuitSignal = options.runTypeXircuitSignal;
    this.lockNodeSignal = options.lockNodeSignal;
    this.reloadAllNodesSignal = options.reloadAllNodesSignal;
    this.toggleAllLinkAnimationSignal = options.toggleAllLinkAnimationSignal;
    this.xircuitsApp = new XircuitsApplication(this.app, this.shell);
  }

  handleEvent(event: Event): void {
    if( event instanceof MouseEvent &&event.type === 'mouseup'){
      // force focus on the editor in order stop key event propagation (e.g. "Delete" key) into unintended
      // parts of jupyter lab.
      this.node.focus();
      // Just to enable back the loses focus event
      this.node.addEventListener('blur', this, true);
    }else if(event.type === 'blur'){
      // Unselect any selected nodes when the editor loses focus
      const deactivate = x => x.setSelected(false);
      const model = this.xircuitsApp.getDiagramEngine().getModel();
      model.getNodes().forEach(deactivate);
      model.getLinks().forEach(deactivate);
    }else if(event.type === 'contextmenu'){
      // Disable loses focus event when opening context menu
      this.node.removeEventListener('blur', this, true);
    } else if (event.type === 'focus') {
      this.focusHandler();
    }
  }

  protected onAfterAttach(msg) {
    this.node.addEventListener('focus', this, true);
    this.node.addEventListener('mouseup', this, true);
    this.node.addEventListener('blur', this, true);
    this.node.addEventListener('contextmenu', this, true);
  }

  protected onBeforeDetach() {
    this.node.removeEventListener('focus', this, true);
    this.node.removeEventListener('mouseup', this, true);
    this.node.removeEventListener('blur', this, true);
    this.node.removeEventListener('contextmenu', this, true);
  }

  private getDiagramModel() {
    return this.xircuitsApp.getDiagramEngine().getModel();
  }

  private async focusHandler() {
    const modelDiagram = this.xircuitsApp.getDiagramEngine().getModel();
    const dataToSend = { 'xircuits_id': modelDiagram.getOptions().id };

    const response = await requestAPI<any>('components_edit/', {
      body: JSON.stringify(dataToSend),
      method: 'POST'
    });

    if (!response['models_exist']) {
      return;
    }

    Object.values(response['models']).map((modelConfig, idx) => {
      const tvbModelNode = modelDiagram.getNode(modelConfig['id']);
      this.updateModelComponentParameters(tvbModelNode, modelConfig['params']);
    });
  }

  private updateModelComponentParameters(modelNode: NodeModel, modelParams) {
    const position_x = modelNode.getX() - 150;
    const position_y = modelNode.getY();
    let position_y_offset = -50;
    Object.values(modelParams).map(param => {
      const param_type = param['type'];
      const param_name = param['name'];

      const ports = modelNode.getPorts();
      for (const port_name in ports) {
        const targetPort = ports[port_name];
        // @ts-ignore
        if (targetPort.getOptions().label === param_name) {
            this.removeLiteralNodesForPort(targetPort);
            position_y_offset += 50;

            const sourcePort = this.createLiteralNodeForParam(
                param_type,
                param['value'].toString(),
                position_x,
                position_y + position_y_offset
            );
            this.addNewLink(sourcePort, targetPort);
            break
          }
      }
    });
  }

  private removeLiteralNodesForPort(targetPort: PortModel) {
    const diagramModel = this.getDiagramModel();
    const targetPortLinks = targetPort.getLinks();

    if (targetPortLinks) {
      Object.values(targetPortLinks).map(link => {
        const sourceNode = link.getSourcePort().getParent();
        sourceNode.getPorts()['out-0'].removeLink(link);
        diagramModel.removeLink(link);
        diagramModel.removeNode(sourceNode);
      });
    }
  }

  private createLiteralNodeForParam(type, value, position_x, position_y) {
    const out_port_name = 'out-0';

    const node = new CustomNodeModel({
      name: 'Literal ' + type.charAt(0).toUpperCase() + type.slice(1),
      color: 'green',
      extras: { type: type }
    });

    node.addOutPortEnhance(value, out_port_name);
    node.setPosition(position_x, position_y);
    this.getDiagramModel().addNode(node);
    return node.getPorts()[out_port_name];
  }

  private addNewLink(source: PortModel, target: PortModel) {
    const newLink = new DefaultLinkModel();
    newLink.setSourcePort(source);
    newLink.setTargetPort(target);
    this.getDiagramModel().addLink(newLink);
  }

  render(): any {
    return (
      <BodyWidget
        context={this.context}
        xircuitsApp={this.xircuitsApp}
        app={this.app}
        shell={this.shell}
        commands={this.commands}
        widgetId={this.parent?.id}
        serviceManager={this.serviceManager}
        fetchComponentsSignal={this.fetchComponentsSignal}
        saveXircuitSignal={this.saveXircuitSignal}
        compileXircuitSignal={this.compileXircuitSignal}
        runXircuitSignal={this.runXircuitSignal}
        runTypeXircuitSignal={this.runTypeXircuitSignal}
        lockNodeSignal={this.lockNodeSignal}
        reloadAllNodesSignal={this.reloadAllNodesSignal}
        toggleAllLinkAnimationSignal={this.toggleAllLinkAnimationSignal}
      />
    );
  }
}
