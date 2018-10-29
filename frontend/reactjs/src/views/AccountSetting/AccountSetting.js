import React, { Component } from 'react';
import {Card, CardHeader, CardBody, Container, Row, Col, InputGroup, InputGroupAddon, InputGroupText, Input, Button} from 'reactstrap';

//stylesheet
import "./style.css";

class AccountSetting extends Component {
  render() {
    return (
      <div className="animated fadeIn mt-5">
        <Container className = "pull-left">
          <Row>
            <Col md = "6">
              <Card>
                <CardHeader>
                  Change Password
                </CardHeader>
                <CardBody>
                  <Row className = "justify-content-center mt-2">
                    <Col md = "8">
                      <InputGroup>
                        <InputGroupAddon addonType="prepend">
                          <InputGroupText>
                            <i className="icon-lock"></i>
                          </InputGroupText>
                        </InputGroupAddon>
                        <Input type="password"  placeholder = "Current Password"/>
                      </InputGroup>
                    </Col>
                  </Row>
                  <Row className = "justify-content-center mt-2">
                    <Col md = "8">
                      <InputGroup>
                        <InputGroupAddon addonType="prepend">
                          <InputGroupText>
                            <i className="fa fa-asterisk"></i>
                          </InputGroupText>
                        </InputGroupAddon>
                        <Input type="password" placeholder = "New Password"/>
                      </InputGroup>
                    </Col>
                  </Row>
                  <Row className = "justify-content-center mt-2">
                    <Col md = "8">
                      <InputGroup>
                        <InputGroupAddon addonType="prepend">
                          <InputGroupText>
                            <i className="fa fa-asterisk"></i>
                          </InputGroupText>
                        </InputGroupAddon>
                        <Input type="password" placeholder = "Confirm Password"/>
                      </InputGroup>
                    </Col>
                  </Row>
                  <Row className = "justify-content-center mt-2">
                      <Button color="primary" active>Change</Button>
                  </Row>
                </CardBody>
              </Card>
            </Col>
          </Row>
          <Row>
            <Col>
                <Card>
                  <CardHeader>
                    Personal Info
                  </CardHeader>
                  <CardBody>
                    <Row className = "mt-2">
                      <Col md = "3" className = "offset-md-1">
                        <InputGroup>
                          <InputGroupAddon addonType="prepend">
                            <InputGroupText className = "inputGroupTextFixed text-right">
                              Name
                            </InputGroupText>
                          </InputGroupAddon>
                          <Input type="text"/>
                        </InputGroup>
                      </Col>
                      <Col md = "3">
                        <InputGroup>
                            <InputGroupAddon addonType="prepend">
                              <InputGroupText className = "inputGroupTextFixed text-right">
                                Job Title
                              </InputGroupText>
                            </InputGroupAddon>
                            <Input type="select">
                              <option>Boss</option>
                              <option>Team Leader</option>
                              <option>Member</option>
                            </Input>
                          </InputGroup>
                      </Col>
                      <Col md = "3">
                        <InputGroup>
                            <InputGroupAddon addonType="prepend">
                              <InputGroupText className = "inputGroupTextFixed text-right">
                                TeamNo
                              </InputGroupText>
                            </InputGroupAddon>
                            <Input type="select">
                              <option>Team 1</option>
                              <option>Team 2</option>
                              <option>Team 3</option>
                            </Input>
                          </InputGroup>
                      </Col>
                    </Row>
                    <Row className = "mt-4">
                      <Col md = "3" className = "offset-md-1">
                        <InputGroup>
                          <InputGroupAddon addonType="prepend">
                            <InputGroupText>
                              Birthday
                            </InputGroupText>
                          </InputGroupAddon>
                          <Input type="date"/>
                        </InputGroup>
                      </Col>
                      <Col md = "6">
                        <InputGroup>
                          <InputGroupAddon addonType="prepend">
                            <InputGroupText>
                              Address
                            </InputGroupText>
                          </InputGroupAddon>
                          <Input type="text"/>
                        </InputGroup>
                      </Col>
                    </Row>
                    <Row className = "mt-4">
                      <Col md = "3" className = "offset-md-1">
                        <InputGroup>
                          <InputGroupAddon addonType="prepend">
                            <InputGroupText>
                              Contact No
                            </InputGroupText>
                          </InputGroupAddon>
                          <Input type="text"/>
                        </InputGroup>
                      </Col>
                      <Col md = "6">
                        <div className = "pull-right">
                          <Button color="primary" active>Update</Button>
                        </div>
                      </Col>
                    </Row>
                  </CardBody>
                </Card>
            </Col>
          </Row>
        </Container>
      </div>
    );
  }
}

export default AccountSetting;
