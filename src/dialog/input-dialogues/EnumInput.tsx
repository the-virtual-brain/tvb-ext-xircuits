import React from "react";
import Dropdown from '../../components/common/Dropdown';

export const EnumInput = ({ title, possibleValues }): JSX.Element => {

  return (
      <div
        style={{
          paddingLeft: 5,
          paddingTop: 5,
          height: '10rem',
          width: '10rem'
        }}
      >
        <Dropdown name={title} types={possibleValues} />
      </div>
  );
};
