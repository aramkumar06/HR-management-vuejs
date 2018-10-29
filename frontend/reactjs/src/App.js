import React, {Component} from "react";
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import { withRouter } from 'react-router-dom';
import { connect } from 'react-redux';

import { loginSuccessAction, logoutSuccessAction} from './actions';
// Styles
// CoreUI Icons Set

// CoreUI Icons Set
import '@coreui/icons/css/coreui-icons.min.css';
// Import Font Awesome Icons Set
import 'font-awesome/css/font-awesome.min.css';
// Import Simple Line Icons Set
import 'simple-line-icons/css/simple-line-icons.css';

// Import Main styles for this application
import './scss/style.css'

//containers
import {DefaultLayout} from './containers'

//Pages
import {Register} from './views/Pages';
import Login from './views/Pages/Login';
import cookie from 'react-cookies';

class App extends Component {
    componentWillMount(){
        let login = cookie.load('login')
        if (login !== undefined) 
            this.props.loginSuccess(login)
        else
            this.props.logoutSuccess();
    }
    render() {
        return (
           <BrowserRouter>
                <Switch>
                    <Route exact path="/login" name="Login Page" component={Login} />
                    <Route exact path="/register" name="Register Page" component={Register} />
                    <Route path="/" name="Home" component={DefaultLayout} />
                </Switch>
           </BrowserRouter>
        );
    }
}

const mapStateToProps = (state) => {
    return {
        login: state.login
    }
}

const mapDispatchToProps = dispatch => ({
    loginSuccess: (payload) => dispatch(loginSuccessAction(payload)),
    logoutSuccess: () => dispatch(logoutSuccessAction())
})

export default withRouter( connect(mapStateToProps, mapDispatchToProps)(App) );