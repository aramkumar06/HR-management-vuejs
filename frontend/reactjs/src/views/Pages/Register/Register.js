import React, { Component } from 'react';

//components
import { Button, Card, CardBody, CardFooter, Col, Container, Form, Input, InputGroup, InputGroupAddon, InputGroupText, Row, UncontrolledTooltip} from 'reactstrap';

//styles
import 'react-day-picker/lib/style.css';

class Register extends Component {

  onCreateAccount = () => {
    console.log("create account");
  }

  render() {
    return (
      <div className="app flex-row align-items-center">
        <Container>
          <Row className="justify-content-center">
            <Col md="6">
              <Card className="mx-4">
                <CardBody className="p-4">
                  <Form onSubmit = {this.onCreateAccount}>
                    <h1>Register</h1>
                    <p className="text-muted">Create your account to HR-Management</p>
                    <InputGroup className="mb-3">
                      <InputGroupAddon addonType="prepend">
                        <InputGroupText>
                          <i className="icon-envelope-letter"></i>
                        </InputGroupText>
                      </InputGroupAddon>
                      <Input type="text" placeholder="Email" autoComplete="email" required/>
                    </InputGroup>
                    <InputGroup className="mb-3">
                      <InputGroupAddon addonType="prepend">
                        <InputGroupText>
                          <i className="icon-lock"></i>
                        </InputGroupText>
                      </InputGroupAddon>
                      <Input type="password" placeholder="Password" autoComplete="new-password" />
                    </InputGroup>
                    <InputGroup className="mb-3">
                      <InputGroupAddon addonType="prepend">
                        <InputGroupText>
                          <i className="icon-lock"></i>
                        </InputGroupText>
                      </InputGroupAddon>
                      <Input type="password" placeholder="Repeat password" autoComplete="new-password" />
                    </InputGroup>
                    <Row>
                      <Col xs="12" sm="6">
                        <InputGroup className="mb-3">
                          <InputGroupAddon addonType="prepend">
                            <InputGroupText>
                              <i className="icon-user"></i>
                            </InputGroupText>
                          </InputGroupAddon>
                          <Input type="text" placeholder="Name" autoComplete="" />
                        </InputGroup>
                      </Col>
                      <Col xs="12" sm="6">
                        <InputGroup className="mb-3">
                          <InputGroupAddon addonType="prepend">
                            <InputGroupText>
                              <i className="icon-calendar"></i>
                            </InputGroupText>
                          </InputGroupAddon>
                          <Input type="date" placeholder="Birthday" id = 'inputBirthday'/>
                        </InputGroup>
                      </Col>
                    </Row>
                    <InputGroup className="mb-3">
                          <InputGroupAddon addonType="prepend">
                            <InputGroupText>
                              <i className="icon-graduation"></i>
                            </InputGroupText>
                          </InputGroupAddon>
                          <Input type="select" name="select" id = "jobTitle">
                            <option>Boss</option>
                            <option>TeamLeader</option>
                            <option>Member</option>
                          </Input>
                    </InputGroup>
                    <InputGroup className="mb-3">
                          <InputGroupAddon addonType="prepend">
                            <InputGroupText>
                              <i className="icon-organization"></i>
                            </InputGroupText>
                          </InputGroupAddon>
                          <Input type="select" name="select" id = "teamNumber">
                            <option>Team 1</option>
                            <option>Team 2</option>
                            <option>Team 3</option>
                          </Input>
                    </InputGroup>
                    <InputGroup className="mb-3">
                          <InputGroupAddon addonType="prepend">
                            <InputGroupText>
                              <i className="icon-location-pin"></i>
                            </InputGroupText>
                          </InputGroupAddon>
                          <Input type="text" placeholder="Address" autoComplete="" />
                    </InputGroup>
                    <InputGroup className="mb-4">
                          <InputGroupAddon addonType="prepend">
                            <InputGroupText>
                              <i className="icon-phone"></i>
                            </InputGroupText>
                          </InputGroupAddon>
                          <Input type="text" placeholder="Contact Number" autoComplete="" />
                    </InputGroup>
                    <Button type = "submit" color="success" block>Create Account</Button>
                  </Form>
                </CardBody>
                <CardFooter className="p-4">
                </CardFooter>
              </Card>
            </Col>
          </Row>
          <UncontrolledTooltip placement="right" target="inputBirthday">
            Your Birthday
          </UncontrolledTooltip>
          <UncontrolledTooltip placement="right" target="jobTitle">
            Job Title
          </UncontrolledTooltip>
          <UncontrolledTooltip placement="right" target="teamNumber">
            Team Number
          </UncontrolledTooltip>
        </Container>
      </div>
    );
  }
}

export default Register;
