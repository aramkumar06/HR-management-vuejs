import React, { Component } from 'react';
import {Card, CardHeader, CardBody, Row, Col, InputGroup, Input, Button, Table, Collapse, FormGroup, Label} from 'reactstrap';

//stylesheet
import "./style.css";

class MyProjects extends Component {
  
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
              <Col md = "8">
                <Card>
                  <CardHeader>
                    Project Add/Edit
                  </CardHeader>
                  <CardBody>
                    <Row>
                      <Col md = "6">
                        <FormGroup>
                          <Label>Project Name</Label>
                          <Input type="text"/>
                        </FormGroup>
                      </Col>
                      <Col md = "6">
                        <FormGroup>
                          <Label>Project URL</Label>
                          <Input type="text"/>
                        </FormGroup>
                      </Col>
                    </Row>
                    <Row className = "">
                      <Col md = "3">
                        <FormGroup>
                          <Label>Client Name</Label>
                          <Input type = "text"/>
                        </FormGroup>
                      </Col>
                      <Col md = "3">
                        <FormGroup>
                          <Label>Project Type</Label>
                          <Input type = "select">
                            <option>Fixed Price</option>
                            <option>Hourly</option>
                          </Input>
                        </FormGroup>
                      </Col>
                      <Col md = "3">
                        <FormGroup>
                          <Label>Project Field</Label>
                          <Input type = "select">
                            <option>Web</option>
                            <option>Mobile</option>
                          </Input>
                        </FormGroup>
                      </Col>
                      <Col md = "3">
                        <FormGroup>
                          <Label>Language/Framework</Label>
                          <Input type = "text"/>
                        </FormGroup>
                      </Col>
                    </Row>
                    <Row>
                      <Col md = "5">
                        <Label>Project Period</Label>
                        <InputGroup>
                          <Input type = "date"/>&nbsp;&nbsp;~&nbsp;&nbsp;
                          <Input type = "date"/>
                        </InputGroup>
                      </Col>
                    </Row>
                    <Row className = "mt-3">
                      <Col>
                        <FormGroup>
                          <Label>Project Description</Label>
                          <Input type="textarea" rows = "5">
                          </Input>
                        </FormGroup>
                      </Col>
                    </Row>
                    <Row>
                      <Col>
                        <div className = "pull-right">
                          <Button color = "primary" onClick = {this.collapse}>Update</Button>
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
                  <th className = "text-center project-type-header"><Button block color="link" onClick={this.unCollapse}><i className = "fa fa-plus fa-x"></i></Button></th>
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
                  <tr onClick={this.unCollapse}>
                    <td className = "text-center">
                      <strong>Hourly</strong>
                    </td>
                    <td className = "text-center">
                      PHP/Laravel Expert
                    </td>
                    <td className = "text-center">
                      Lancelot Gordon
                    </td>
                    <td className = "text-center">
                      Web Development
                    </td>
                    <td className = "text-center">
                      Laravel
                    </td>
                    <td className = "text-center">
                      2018.8.30 ~ 2018.9.2
                    </td>
                  </tr>
                  <tr onClick={this.unCollapse}>
                    <td className = "text-center">
                      <strong>Hourly</strong>
                    </td>
                    <td className = "text-center">
                      Magento Theme modification
                    </td>
                    <td className = "text-center">
                      Marek12
                    </td>
                    <td className = "text-center">
                      Web Development
                    </td>
                    <td className = "text-center">
                      Magento
                    </td>
                    <td className = "text-center">
                      2018.8.30 ~ 2018.9.10
                    </td>
                  </tr>
                  <tr onClick={this.unCollapse}>
                    <td className = "text-center">
                      <strong>Fixed</strong>
                    </td>
                    <td className = "text-center">
                      CSV Import Export
                    </td>
                    <td className = "text-center">
                      becomevocal
                    </td>
                    <td className = "text-center">
                      Web Development
                    </td>
                    <td className = "text-center">
                      Javascript
                    </td>
                    <td className = "text-center">
                      2018.9.10 ~ 2018.9.13
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

export default MyProjects;
