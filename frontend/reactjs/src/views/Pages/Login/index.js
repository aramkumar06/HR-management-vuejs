import React, { Component } from 'react';
import axios from 'axios';
import { withRouter } from 'react-router-dom';
import { connect } from 'react-redux';
import { loginSuccessAction } from '../../../actions';
import {AuthUrls} from '../../../constants/urls';
import LoginForm from './LoginForm';
import cookie from 'react-cookies';

class Login extends Component {

    state = {
        errors: ''
    }

    componentDidMount() {
        window.scrollTo(0, 0)
    }

    handleLogin = (values) => {      
        axios.post(AuthUrls.LOGIN, values)
        .then(response => { 
            this.props.loginSuccess(response.data)
            if (response.data.success === true) {
                cookie.save('login', response.data, { path: '/', maxAge: 3600 * 24 * 7 })
                this.setState({
                    success: 'Login success',
                    error: '',
                })
                this.props.history.push('/')
            } else {
                this.setState({
                    errors: 'Username or Password Invalid!',
                })
                this.props.history.push('/login')
            }
        })
        .catch(error => {
            this.setState({
                errors: error.response.data.error,
            })
        });
    }

    handleKeyEvent = (event) => {
        if (event.charCode === 13 || event.keyCode === 13) {
            this.login();
        }
    }

    render() {
        return (
            <LoginForm onSubmit={this.handleLogin} errors={this.state.errors} success={this.state.success} history = {this.props.history}/>
        )
    }
}

const mapStateToProps = (state) => {
    return {
        login: state.login
    }
}

const mapDispatchToProps = dispatch => ({
    loginSuccess: (payload) => dispatch(loginSuccessAction(payload)),
})

export default withRouter( connect(mapStateToProps, mapDispatchToProps)(Login) );
