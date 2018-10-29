import React from "react";
import {InputGroup, InputGroupAddon, InputGroupText, Input} from 'reactstrap';
export const renderField = ({ input, icon, type, required }) => (
    <InputGroup>
        <InputGroupAddon addonType="prepend">
            <InputGroupText>
                <i className = {icon}></i>
            </InputGroupText>
        </InputGroupAddon>
        <Input className="form-control" {...input} type={type} required = {required}/>
    </InputGroup>
);

export const renderTextAreaField = ({ input, label, type, meta: { touched, error } }) => (
    <div>
        <label>{label}</label>
        <div>
            <textarea className="form-control" {...input} type={type}/>
        </div>
        {touched && ((error && <div className="alert alert-danger p-1"><small>{error}</small></div>))}
    </div>
);

export const renderError = (errorMessages) => {
    if ( errorMessages) {
        return (
            <div className="alert alert-danger">
                {errorMessages}
            </div>
        )
    }
};
