import React, {Component} from "react";
import { HashRouter, Route, Switch } from 'react-router-dom';

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
import {Login, Register} from './views/Pages';

class App extends Component {
    render() {
        return (
           <HashRouter>
                <Switch>
                    <Route exact path="/login" name="Login Page" component={Login} />
                    <Route exact path="/register" name="Register Page" component={Register} />
                    <Route path="/" name="Home" component={DefaultLayout} />
                </Switch>
           </HashRouter>
        );
    }
}

export default App;