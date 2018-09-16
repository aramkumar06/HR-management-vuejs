import React, { Component } from 'react';
import PropTypes from 'prop-types';

import { AppSidebarToggler } from '@coreui/react';

const logo_image_url = "assets/imgs/portal-logo1.png";
const style = {
  logo:{
    width: 130,
    height: 40
  }
}
const propTypes = {
  children: PropTypes.node,
};

const defaultProps = {};

class DefaultHeader extends Component {
  render() {

    // eslint-disable-next-line
    const { children, ...attributes } = this.props;

    return (
      <React.Fragment>
        <img src = {logo_image_url} alt = "HR-Management" style = {style.logo}/>
        <AppSidebarToggler className="d-md-down-none" display="lg" />
      </React.Fragment>
    );
  }
}

DefaultHeader.propTypes = propTypes;
DefaultHeader.defaultProps = defaultProps;

export default DefaultHeader;
