import { ReactWidget } from '@jupyterlab/apputils';
import { HTMLSelect } from '@jupyterlab/ui-components';
import React from 'react';
import { XpipeFactory } from '../xpipeFactory';

/**
 * A toolbar widget that switches output types.
 */
export class RunSwitcher extends ReactWidget {
    /**
     * Construct a new output type switcher.
     */
    constructor(widget: XpipeFactory) {
        super();
        this._output = widget;
    }

    /**
     * Handle `change` events for the HTMLSelect component.
     */
    handleChange = (event: React.ChangeEvent<HTMLSelectElement>): void => {
        let runType = event.target.value;
        this._output.runTypeXpipeSignal.emit({ runType })

        this.update();
    };

    render() {
        let value;
        return (
            <HTMLSelect
                onChange={this.handleChange}
                value={value}
                aria-label={'Run type'}
                title={'Select the run type'}
            >
                <option value="run" >Run</option>
                <option value="run-dont-compile">Run w/o Compile</option>
                <option value="spark-submit">Spark Submit</option>
            </HTMLSelect>
        );
    }
    private _output: XpipeFactory;
}