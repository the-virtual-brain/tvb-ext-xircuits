import * as React from "react";
import Toggle from 'react-toggle'
import {useCallback, useRef} from "react";
import {WithToggleProps} from "./types";
import ToolTip from 'react-portal-tooltip';


export default function WithToggle(props: WithToggleProps){
	const ref = useRef(null);

	const changeHandler = useCallback(() => {
		props.setShowDescription(!props.showDescription)
		props.setDescriptionStr(props.description)
	}, [props.description, props.showDescription])

	return (
		<div ref ={ref} className="alignToggle">
			{props.renderToggleBeforeChildren ?
				<>
					{
						props.description &&
							<Toggle
								className='description'
								name='Description'
								checked={props.showDescription}
								onChange={changeHandler}
							/>
					}
					<span style={{display: "inline-block", paddingLeft: "0.3rem"}}>
						{props.children}
					</span>
				</>
				:
				<>
					<span style={{display: "inline-block", paddingRight: "0.3rem"}}>
						{props.children}
					</span>
					{
						props.description &&
							<Toggle
								className='description'
								name='Description'
								checked={props.showDescription}
								onChange={changeHandler}
							/>
					}
				</>
			}
		</div>
	)
}