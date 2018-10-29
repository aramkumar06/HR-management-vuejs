import React, { Component } from 'react';
import { DropdownItem, DropdownMenu, DropdownToggle, Nav} from 'reactstrap';
import cookie from 'react-cookies';
import { AppSidebarToggler, AppHeaderDropdown} from '@coreui/react';
import { withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import { logoutSuccessAction} from '../../actions';

class DefaultHeader extends Component {

  onLogOut = () =>{
    cookie.remove('login', { path: '/' })
    this.props.logoutSuccess();
    this.props.history.push("/login");
  }

  render() {

    // eslint-disable-next-line
    const { children, ...attributes } = this.props;

    return (
      <React.Fragment>
        <AppSidebarToggler className="d-md-down-none" display="lg" />
        <Nav className="ml-auto" navbar>
          <AppHeaderDropdown direction="down">
            <DropdownToggle nav>
              <img src={'assets/img/avatars/1.png'} className="img-avatar" alt="Menu" />
            </DropdownToggle>
            <DropdownMenu right style={{ right: 'auto' }}>
              <DropdownItem><i className="fa fa-user-circle"></i>Account Setting</DropdownItem>
              <DropdownItem onClick = {this.onLogOut}><i className="fa fa-sign-out"></i>Log Out</DropdownItem>
            </DropdownMenu>
          </AppHeaderDropdown>
        </Nav>
      </React.Fragment>
    );
  }
}

const mapDispatchToProps = dispatch => ({
  logoutSuccess: () => dispatch(logoutSuccessAction())
})

export default withRouter( connect(null, mapDispatchToProps)(DefaultHeader) );