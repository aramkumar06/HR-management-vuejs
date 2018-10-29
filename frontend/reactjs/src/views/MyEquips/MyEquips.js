import React, { Component } from 'react';
import {Card, CardHeader, CardBody, Row, Col, Input, Button, Table, Collapse, FormGroup, Label} from 'reactstrap';

//stylesheet
import "./style.css";

class MyEquips extends Component {
  
  constructor(props) {
    super(props);
    this.state = { collapse: false };
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
                    Equipment Add/Edit
                  </CardHeader>
                  <CardBody>
                    <Row>
                      <Col md = "3">
                        <FormGroup>
                          <Label>Name</Label>
                          <Input type = "select">
                            <option>Desktop</option>
                            <option>Laptop</option>
                            <option>BroadBand</option>
                            <option>Phone</option>
                            <option>SimCard</option>
                          </Input>
                        </FormGroup>
                      </Col>
                      <Col md = "3">
                        <FormGroup>
                          <Label>Model</Label>
                          <Input type = ""/>
                        </FormGroup>
                      </Col>
                      <Col md = "6">
                        <FormGroup>
                          <Label>Specifications</Label>
                          <Input type = ""/>
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
            <Col md = "1">
              <Button block color="link" onClick={this.unCollapse}>Add Equipment</Button>
            </Col>
          </Row>
          <Row>
            <Col>
            <div className = "table-wrapper">
              <Table hover bordered responsive className="table-outline mb-0 d-none d-sm-table">
                  <thead className="thead-light">
                  <tr>
                    <th className = "text-center name-header">Name</th>
                    <th className="text-center model-header">Model</th>
                    <th className = "text-center specification-header">Specifications</th>
                  </tr>
                  </thead>
                  <tbody>
                    <tr onClick={this.unCollapse}>
                      <td className = "text-center">
                        <strong>Desktop</strong>
                      </td>
                      <td className = "text-center">
                        Acer
                      </td>
                      <td className = "text-center">
                        Core i5 7th Gen, 8G RAM, HDD 1TB, Display LG.23'
                      </td>
                    </tr>
                    <tr onClick={this.unCollapse}>
                      <td className = "text-center">
                        <strong>Desktop</strong>
                      </td>
                      <td className = "text-center">
                        Dexsp
                      </td>
                      <td className = "text-center">
                        Core i5 7th Gen, 8G RAM, HDD 1TB, NVDIA 1GB, Display LG.23'
                      </td>
                    </tr>
                    <tr onClick={this.unCollapse}>
                      <td className = "text-center">
                        <strong>Desktop</strong>
                      </td>
                      <td className = "text-center">
                        Laptop
                      </td>
                      <td className = "text-center">
                        Core i5 7th Gen, 4G RAM, HDD 2TB
                      </td>
                    </tr>
                    <tr onClick={this.unCollapse}>
                      <td className = "text-center">
                        <strong>Brodband</strong>
                      </td>
                      <td className = "text-center">
                        Megafon
                      </td>
                      <td className = "text-center">
                      </td>
                    </tr>
                  </tbody>
              </Table>
            </div>
          </Col>
          </Row>
      </div>
    );
  }
}

export default MyEquips;
