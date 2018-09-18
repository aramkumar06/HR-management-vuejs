import React, { Component } from 'react';
import {Card, CardHeader, CardBody, Row, Col, InputGroup, InputGroupAddon, InputGroupText, Input, Button, Table, Collapse} from 'reactstrap';

//stylesheet
import "./style.css";

class MyContacts extends Component {
  
  constructor(props) {
    super(props);
    this.state = { collapse: true };
    this.unCollapse = this.unCollapse.bind(this);
    this.collapse = this.collapse.bind(this);
  }

  unCollapse() {
    this.setState({
      collapse: false
    });
  }

  collapse(){
    this.setState({
      collapse: true
    });
  }

  render() {
    return (
      <div className="animated fadeIn mt-5">
          <Collapse isOpen={!this.state.collapse}>
            <Row>
              <Col>
                <Card>
                  <CardHeader>
                    Contact Info Add/Edit
                  </CardHeader>
                  <CardBody>
                  <Row>
                    <Col md = "3" className = "offset-md-1">
                      <InputGroup>
                        <InputGroupAddon addonType="prepend">
                          <InputGroupText>
                            Contact Type
                          </InputGroupText>
                        </InputGroupAddon>
                        <Input type="select">
                          <option>Upwork</option>
                          <option>Freelancer</option>
                          <option>E-Mail</option>
                          <option>Skype</option>
                          <option>Github</option>
                          <option>Facebook</option>
                          <option>Linkedin</option>
                        </Input>
                      </InputGroup>
                    </Col>
                    <Col md = "3">
                      <InputGroup>
                        <InputGroupAddon addonType="prepend">
                            <InputGroupText>
                              Username
                            </InputGroupText>
                        </InputGroupAddon>
                        <Input type = "text"/>
                      </InputGroup>
                    </Col>
                    <Col md = "3">
                      <InputGroup>
                        <InputGroupAddon addonType="prepend">
                            <InputGroupText>
                              Password
                            </InputGroupText>
                        </InputGroupAddon>
                        <Input type = "text"/>
                      </InputGroup>
                    </Col>
                  </Row>
                  <Row className = "mt-3">
                    <Col md = "5" className = "offset-md-1">
                      <InputGroup>
                        <InputGroupAddon addonType="prepend">
                            <InputGroupText>
                              Security Qeustion
                            </InputGroupText>
                        </InputGroupAddon>
                        <Input type = "text"/>
                      </InputGroup>
                    </Col>
                    <Col md = "4">
                      <InputGroup>
                        <InputGroupAddon addonType="prepend">
                            <InputGroupText>
                              Security Answer
                            </InputGroupText>
                        </InputGroupAddon>
                        <Input type = "text"/>
                      </InputGroup>
                    </Col>
                    <Col md = "2">
                      <div>
                        <Button color="primary" active onClick={this.collapse}>Add</Button>
                      </div>
                    </Col>

                  </Row>
                  </CardBody>
                </Card>
              </Col>
            </Row>
          </Collapse>
          <Row>
            <Col>
              <Card>
              <Table hover bordered responsive className="table-outline mb-0 d-none d-sm-table">
                <thead className="thead-light">
                <tr>
                  <th className = "text-center contact-icon-header"><Button block color="link" onClick={this.unCollapse}><i className = "fa fa-plus fa-x"></i></Button></th>
                  <th className="text-center">Contact Type</th>
                  <th className = "text-center">UserName</th>
                  <th className="text-center">Password</th>
                </tr>
                </thead>
                <tbody>
                  <tr onClick={this.unCollapse}>
                    <td className = "text-center">
                      <i className = "fa fa-user-md fa-2x"></i>
                    </td>
                    <td className = "text-center">
                      <strong>Freelancer</strong>
                    </td>
                    <td className = "text-center">
                      ipullar
                    </td>
                    <td className = "text-center">
                      ******************
                    </td>
                  </tr>
                  <tr onClick={this.unCollapse}>
                    <td className = "text-center">
                      <i className = "fa fa-skype fa-2x"></i>
                    </td>
                    <td className = "text-center">
                      <strong>Skype</strong>
                    </td>
                    <td className = "text-center">
                      sergeyhopesome@gmail.com
                    </td>
                    <td className = "text-center">
                      ******************
                    </td>
                  </tr>
                  <tr onClick={this.unCollapse}>
                    <td className = "text-center">
                      <i className = "fa fa-envelope fa-2x"></i>
                    </td>
                    <td className = "text-center">
                      <strong>E-Mail</strong>
                    </td>
                    <td className = "text-center">
                      sergeyhopesome@gmail.com
                    </td>
                    <td className = "text-center">
                      ******************
                    </td>
                  </tr>
                  <tr onClick={this.unCollapse}>
                    <td className = "text-center">
                      <i className = "fa fa-github fa-2x"></i>
                    </td>
                    <td className = "text-center">
                      <strong>Github</strong>
                    </td>
                    <td className = "text-center">
                      keepgoingdev
                    </td>
                    <td className = "text-center">
                      ******************
                    </td>
                  </tr>
                  <tr onClick={this.unCollapse}>
                    <td className = "text-center">
                      <i className = "fa fa-facebook fa-2x"></i>
                    </td>
                    <td className = "text-center">
                      <strong>Facebook</strong>
                    </td>
                    <td className = "text-center">
                      keepgoingman
                    </td>
                    <td className = "text-center">
                      ******************
                    </td>
                  </tr>
                  <tr onClick={this.unCollapse}>
                    <td className = "text-center">
                      <i className = "fa fa-linkedin fa-2x"></i>
                    </td>
                    <td className = "text-center">
                      <strong>Linkedin</strong>
                    </td>
                    <td className = "text-center">
                      acharusin810
                    </td>
                    <td className = "text-center">
                      ******************
                    </td>
                  </tr>
                </tbody>
            </Table>
            </Card>
          </Col>
          </Row>
      </div>
    );
  }
}

export default MyContacts;
