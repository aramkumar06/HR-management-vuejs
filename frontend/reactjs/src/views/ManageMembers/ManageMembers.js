import React, { Component } from 'react';
import {Card, CardHeader, CardBody, Row, Col, InputGroup, InputGroupAddon, InputGroupText,Input, Button, Table, Collapse, FormGroup, Label} from 'reactstrap';

//stylesheet
import "./style.css";

class ManageMembers extends Component {
  
  constructor(props) {
    super(props);
    this.state = { collapse: false };
    this.toggle = this.toggle.bind(this);
  }

  toggle() {
    this.setState({
      collapse: !this.state.collapse
    });
  }

  render() {
    return (
      <div className="animated fadeIn mt-5">
            <Row>
              <Col md = "8">
                <Card>
                  <CardHeader>
                    <Button color = "link" onClick = {this.toggle}><h5>Project Search</h5></Button>
                  </CardHeader>
                  <Collapse isOpen={!this.state.collapse}>
                    <CardBody>
                      <Row>
                        <Col md = "3">
                          <FormGroup>
                            <Label>
                              Project Name
                            </Label>
                            <Input type = "text"></Input>
                          </FormGroup>
                        </Col>
                        <Col md = "5">
                          <Label>Project Period</Label>
                          <InputGroup>
                            <Input type = "date"/>&nbsp;&nbsp;~&nbsp;&nbsp;
                            <Input type = "date"/>
                          </InputGroup>
                        </Col>
                      </Row>
                      <Row>
                        <Col md = "3">
                          <FormGroup>
                            <Label>Project Type</Label>
                            <Input type = "select">
                              <option>Fixed</option>
                              <option>Hourly</option>
                            </Input>
                          </FormGroup>
                        </Col>
                        <Col md = "3">
                          <FormGroup>
                            <Label>Project Type</Label>
                            <Input type = "select">
                              <option>Mobile Development</option>
                              <option>Web Development</option>
                            </Input>
                          </FormGroup>
                        </Col>
                        <Col md = "3">
                          <FormGroup>
                            <Label>Language/Framework</Label>
                            <Input type = "text">
                            </Input>
                          </FormGroup>
                        </Col>
                      </Row>
                      <Row>
                        <Col md = "2">
                          <InputGroup>
                            <Input type="select">
                              <option>Company</option>
                              <option>Team</option>
                              <option>User</option>
                            </Input>
                          </InputGroup>
                        </Col>
                        <Col md = "2">
                          <InputGroup>
                            <Input type="select">
                              <option>Team1</option>
                              <option>Team2</option>
                              <option>Team3</option>
                            </Input>
                          </InputGroup>
                        </Col>
                        <Col md = "2">
                          <InputGroup>
                            <Input type="select">
                              <option>Alexar</option>
                              <option>Victor</option>
                              <option>Pabel</option>
                            </Input>
                          </InputGroup>
                        </Col>
                        <Col md = "2">
                          <InputGroup>
                            <Input type="select">
                              <option>Monthly</option>
                              <option>Weekly</option>
                            </Input>
                          </InputGroup>
                        </Col>
                        <Col md = "2">
                          <Button color = "primary">Search</Button>
                        </Col>
                      </Row>
                    </CardBody>
                  </Collapse>
                </Card>
              </Col>
            </Row>
          <Row>
            <Col>
              <Card>
              <Table hover bordered responsive className="table-outline mb-0 d-none d-sm-table">
                <thead className="thead-light">
                <tr>
                  <th className = "text-center project-type-header">Project Type</th>
                  <th className="text-center project-name-header">Project Name</th>
                  <th className = "text-center client-name-header">Client Name</th>
                  <th className = "text-center project-field-header">Project Field</th>
                  <th className = "text-center language-header">Language / Framework</th>
                  <th className="text-center project-period-header">Project Period</th>
                </tr>
                </thead>
                <tbody>
                  <tr onClick={this.unCollapse}>
                    <td className = "text-center">
                      <strong>Fixed</strong>
                    </td>
                    <td className = "text-center">
                      Wordpress Theme modification
                    </td>
                    <td className = "text-center">
                      Julian.W
                    </td>
                    <td className = "text-center">
                      Software Development
                    </td>
                    <td className = "text-center">
                      Wordpress
                    </td>
                    <td className = "text-center">
                      2018.9.13 ~ 2018.9.15
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

export default ManageMembers;
