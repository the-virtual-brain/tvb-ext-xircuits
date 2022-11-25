import {ReactElement} from "react";

export type WithToggleProps = {
    renderToggleBeforeChildren : boolean;
    children: ReactElement[] | ReactElement | string;
    showDescription: boolean;
    setShowDescription: any;
    description: string;
}

export type WithToggleState = {
    showDescription : boolean
}