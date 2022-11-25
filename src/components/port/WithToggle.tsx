import * as React from "react";
import Toggle from 'react-toggle'
import {useRef} from "react";
import {WithToggleProps} from "./types";
import ToolTip from 'react-portal-tooltip';


export default function WithToggle(props: WithToggleProps){
	const ref = useRef(null);

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
								onChange={() => props.setShowDescription(!props.showDescription)}
							/>
					}
					<span>
						{props.children}
					</span>
				</>
				:
				<>
					<span>
						{props.children}
					</span>
					{
						props.description &&
							<Toggle
								className='description'
								name='Description'
								checked={props.showDescription}
								onChange={() => props.setShowDescription(!props.showDescription)}
							/>
					}
				</>
			}

			{props.showDescription &&
				<ToolTip active={props.showDescription} position="left" arrow="center" parent={ref.current}>
					<div>{props.description}</div>
				</ToolTip>
			}
		</div>
	)
}