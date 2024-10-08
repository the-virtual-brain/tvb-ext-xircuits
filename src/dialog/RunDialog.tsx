import * as NumericInput from "react-numeric-input";
import TextareaAutosize from 'react-textarea-autosize';
import React, { useEffect, useState } from 'react';
import Switch from "react-switch";
import { HTMLSelect } from "@jupyterlab/ui-components";
import { useCollapse } from 'react-collapsed';
import { writeDefaultSite } from "../siteUtils";

export const RunDialog = ({
	runTypes,
	runConfigs,
	lastConfig,
	childStringNodes,
	childBoolNodes,
	childIntNodes,
	childFloatNodes
}): JSX.Element => {

	const [checked, setChecked] = useState<boolean[]>([false]);
	const [runType, setRunType] = useState("");
	const [runConfig, setRunConfig] = useState("DAINT-CSCS");
	const [command, setCommand] = useState("");
	const [filesystem, setFilesystem] = useState("HOME");
	const [python, setPython] = useState("python3.9");
	const [modules, setModules] = useState("cray-python");

	const handleChecked = (e, i) => {
		let newChecked = [...checked];
		newChecked[i] = e;
		setChecked(newChecked);
		console.log("Boolean change: ", checked)
	};

	/**
	 * Handle `change` events for the HTMLSelect component of run type.
	 */
	const handleTypeChange = (event: React.ChangeEvent<HTMLSelectElement>): void => {
		let type = event.target.value;
		setRunType(type);
		setRunConfig("-");
		setCommand("");
	};

	/**
	 * Handle `change` events for the HTMLSelect component for run config.
	 */
	const handleConfigChange = (event: React.ChangeEvent<HTMLSelectElement>): void => {
		let configName = event.target.value;
		writeDefaultSite(configName);
		setRunConfig(configName);
		if (configName == "-") {
			setCommand("");
		}
		if (configName == "JUSUF") {
			setFilesystem('PROJECT');
			setPython('python3.10');
			setModules('Python');
		} else {
			setFilesystem('HOME');
			setPython('python3.9');
			setModules("cray-python");
		}
	};

	useEffect(() => {
		if (runTypes.length != 0) {
			setRunType(runTypes[0].run_type);
		}

		if (lastConfig.length != 0) {
			setRunType(lastConfig.run_type);
			setRunConfig(lastConfig.run_config_name);
			setCommand(lastConfig.command);
		}
	}, [])

	useEffect(() => {
		if (runConfigs.length != 0) {
			runConfigs.map(c => {
				if (c.run_config_name == runConfig) setCommand(c.command);
			})
		}
	}, [runConfig])

	function Collapsible() {
    	const { getCollapseProps, getToggleProps, isExpanded } = useCollapse();
		return (
		<div className="collapsible">
			<div className="header" {...getToggleProps()}>
				{isExpanded ? 'Advanced setup' : 'Advanced setup'}
				<div className="icon">
                	<i className={'fas fa-chevron-circle-' + (isExpanded ? 'up' : 'down')}></i>
            </div>
			</div>
			<div {...getCollapseProps()}>
				<div>
					Filesystem:
					<div>
						<input
							name='filesystem'
							defaultValue={filesystem}
							title={'Filesystem to use on HPC for preparing the environment'}
							style={{ width: 300, fontSize: 13 }}/>
					</div>
					Python dir:
					<div>
						<input
							name='python'
							defaultValue={python}
							title={'Python directory to use on HPC'}
							style={{ width: 300, fontSize: 13 }}/>
					</div>
					Modules to load:
					<div>
						<input
							name='modules'
							defaultValue={modules}
							title={'Modules to load on HPC'}
							style={{ width: 300, fontSize: 13 }}/>
					</div>
					Libraries to install:
					<div>
						<input
							name='libraries'
							defaultValue={'tvb-ext-xircuits tvb-data'}
							title={'Libraries to install on HPC'}
							style={{ width: 300, fontSize: 13 }}/>
					</div>
				</div>
			</div>
		</div>
		);
	}

	return (
		<form>
			<div>{runConfigs.length != 0 ?
				<><h3 style={{ marginTop: 2, marginBottom: 0 }}>Remote Execution</h3>
					<div>Available Run Type:
						<HTMLSelect
							onChange={(e) => handleTypeChange(e)}
							value={runType}
							aria-label={'Available Run Types'}
							title={'Select the run type'}
							name='runType'
						>
							{runTypes.map((type, i) => (
								<option id={type.id} key={`index-type-${i}`} value={type.run_type}>
									{(type.run_type)}
								</option>
							))}
						</HTMLSelect>
					</div>
					<div>Available Run Sites:
						<HTMLSelect
							onChange={(e) => handleConfigChange(e)}
							value={runConfig}
							aria-label={'Available Run Sites'}
							title={'Select on which site to run'}
							name='runConfig'
						>
							{runConfigs.map((c, i) => ((c.run_type == runType) ?
								<option id={c.id} key={`index-config-${i}`} value={c.run_config_name}>
									{(c.run_config_name)}
								</option> : null
							))}
						</HTMLSelect>
					</div>
					Project:
					<div>
						<input
							name='project'
							title={'Project account to use on the HPC site chosen above'}
							style={{ width: 300, fontSize: 13 }} />
					</div>
					Launch monitoring HPC:
					<div>
						<input type={'checkbox'}
							title={'If checked, the HPC monitoring widget is opened up automatically in a new tab. This can be accessed from the Monitor HPC button as well.'}
							name='monitoring'
						>
						</input>
					</div>
					Stage-out results:
					<div>
						<input type={'checkbox'}
							title={'If checked, the workflow waits for all HPC jobs to finish and stages-out the results. Otherwise, they can be downloaded manually from the HPC monitoring widget.'}
							name='stage-out'
						>
						</input>
					</div>
					<Collapsible/>
				</>
				: null}
			</div>
			<div></div>
			{/*<div><h4 style={{ marginTop: 2, marginBottom: 0 }}>String</h4></div>*/}
			{childStringNodes.map((stringNode, i) =>
				<div key={`index-${i}`}>{stringNode}
					<div>
						<input
							type="text"
							name={stringNode}
							style={{ width: 300, fontSize: 13 }}
						/>
					</div>
				</div>)}
			<div>
				{
					childBoolNodes.length != 0 ?
						<><br /><h4 style={{ marginTop: 2, marginBottom: 0 }}>Boolean</h4></> : null
				}
			</div>
			{childBoolNodes.map((boolNode, i) =>
				<div key={`index-${i}`}>{boolNode}
					<div>
						<Switch
							checked={checked[i] ?? true}
							name={boolNode}
							onChange={(e) => handleChecked(e, i)}
							handleDiameter={25}
							height={20}
							width={48}
						/>
					</div>
				</div>)}
			<div>
				{
					childIntNodes.length != 0 ?
						<><br /><h4 style={{ marginTop: 2, marginBottom: 0 }}>Integer</h4></> : null
				}
			</div>
			{childIntNodes.map((intNode, i) =>
				<div key={`index-${i}`}>{intNode}
					<div>
						<NumericInput
							className="form-control"
							name={intNode}
							value={'0'}
							min={0}
							step={1}
							precision={0}
							mobile={true}
							style={{
								wrap: {
									boxShadow: '0 0 1px 1px #fff inset, 1px 1px 5px -1px #000',
									padding: '2px 2.26ex 2px 2px',
									borderRadius: '6px 3px 3px 6px',
									fontSize: 20,
									width: '60%'
								},
								input: {
									borderRadius: '6px 3px 3px 6px',
									padding: '0.1ex 1ex',
									border: '#ccc',
									marginRight: 4,
									display: 'block',
									fontWeight: 100,
									width: '100%'
								},
								plus: {
									background: 'rgba(255, 255, 255, 100)'
								},
								minus: {
									background: 'rgba(255, 255, 255, 100)'
								},
								btnDown: {
									background: 'rgba(0, 0, 0)'
								},
								btnUp: {
									background: 'rgba(0, 0, 0)'
								}
							}}
						/>
					</div>
				</div>)}
			<div>
				{
					childFloatNodes.length != 0 ?
						<><br /><h4 style={{ marginTop: 2, marginBottom: 0 }}>Float</h4></> : null
				}
			</div>
			{childFloatNodes.map((floatNode, i) =>
				<div className="p-col-12" key={`index-${i}`}>{floatNode}
					<div>
						<NumericInput
							className="form-control"
							name={floatNode}
							value={'0.00'}
							min={0}
							step={0.1}
							precision={2}
							mobile={true}
							style={{
								wrap: {
									boxShadow: '0 0 1px 1px #fff inset, 1px 1px 5px -1px #000',
									padding: '2px 2.26ex 2px 2px',
									borderRadius: '6px 3px 3px 6px',
									fontSize: 20,
									width: '60%'
								},
								input: {
									borderRadius: '6px 3px 3px 6px',
									padding: '0.1ex 1ex',
									border: '#ccc',
									marginRight: 4,
									display: 'block',
									fontWeight: 100,
									width: '100%'
								},
								plus: {
									background: 'rgba(255, 255, 255, 100)'
								},
								minus: {
									background: 'rgba(255, 255, 255, 100)'
								},
								btnDown: {
									background: 'rgba(0, 0, 0)'
								},
								btnUp: {
									background: 'rgba(0, 0, 0)'
								}
							}}
						/>
					</div>
				</div>)}
		</form>
	);
}
