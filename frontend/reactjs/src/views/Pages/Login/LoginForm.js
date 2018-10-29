import React from 'react';
import { Button, Card, CardBody, CardGroup, Col, Container, Form, Row } from 'reactstrap';
import { reduxForm, Field } from "redux-form";

//Include
import { renderField} from "../../../utils/renderUtils";

const LoginForm = (props) =>{
  const {handleSubmit, submitting, errors, history} = props

  const handleKeyEvent = (event) => {
    if (event.charCode === 13 || event.keyCode === 13) {
        handleSubmit()
    }
  }

  const onRegister = () => {
    history.push("/register");
  }

  return (
      <div className="app flex-row align-items-center">
        <Container>
          <Row className="justify-content-center">
            <Col md="8">
              <CardGroup>
                <Card className="p-4">
                  <CardBody>
                    <Row className = "mb-3">
                      <Col>
                        {errors && 
                          <div className="alert alert-danger">{errors}</div>
                        }
                      </Col>
                    </Row>
                    <Form onSubmit={handleSubmit}>
                      <h1>Login</h1>
                      <p className="text-muted">Sign In to HR-Management</p>
                        <fieldset className = "mb-3">
                          <Field type="text" icon = "icon-user" placeholder="Username" name = "username" component={renderField} required handleKeyEvent={handleKeyEvent}/>
                        </fieldset>
                        <fieldset className = "mb-3">
                        <Field type="password" icon = "icon-lock" placeholder="Password" name = "password" component={renderField} required handleKeyEvent={handleKeyEvent}/>
                        </fieldset>
                      <Row>
                        <Col xs="8">
                        </Col>
                        <Col xs="4">
                          <Button color="primary" className="px-4 pull-right" action = "submit" disabled={submitting}>Login</Button>
                        </Col>
                      </Row>
                    </Form>
                  </CardBody>
                </Card>
                <Card className="text-white bg-primary py-5 d-md-down-none" style={{ width: 44 + '%' }}>
                  <CardBody className="text-center">
                    <div>
                      <h2>Sign up</h2>
                      <p>If you don't have your account, please create one. <br></br>It's free.<i className = "icon-emotsmile"></i></p>
                      <Button color="primary" className="mt-3" onClick = {onRegister} active>Register Now!</Button>
                    </div>
                  </CardBody>
                </Card>
              </CardGroup>
            </Col>
          </Row>
        </Container>
      </div>
    );
}

export default reduxForm({
  form: 'loginForm', // a unique identifier for this form
})(LoginForm)
