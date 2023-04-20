import React from "react";


function Dropdown(props: {name: string, types : string[]}){

    return (
        <select name={props.name}>
            {
                props.types.map(
                    (type, index) => <option value={type} key={index}>{type}</option>
                )
            }
        </select>
    )
}

export default Dropdown;