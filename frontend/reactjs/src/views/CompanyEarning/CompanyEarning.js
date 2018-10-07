import React, { Component } from 'react';
import { Card, CardBody, CardHeader, Row, Col, InputGroup, InputGroupAddon, InputGroupText, Input, Label, Table, Badge} from 'reactstrap';
import { Line, Bar} from 'react-chartjs-2';
import { CustomTooltips } from '@coreui/coreui-plugin-chartjs-custom-tooltips';

//style
import './style.css';

//Chart Data
const line = {
  labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
  datasets: [
    {
      label: 'My First dataset',
      fill: false,
      lineTension: 0.1,
      backgroundColor: 'rgba(75,192,192,0.4)',
      borderColor: 'rgba(75,192,192,1)',
      borderCapStyle: 'butt',
      borderDash: [],
      borderDashOffset: 0.0,
      borderJoinStyle: 'miter',
      pointBorderColor: 'rgba(75,192,192,1)',
      pointBackgroundColor: '#fff',
      pointBorderWidth: 1,
      pointHoverRadius: 5,
      pointHoverBackgroundColor: 'rgba(75,192,192,1)',
      pointHoverBorderColor: 'rgba(220,220,220,1)',
      pointHoverBorderWidth: 2,
      pointRadius: 1,
      pointHitRadius: 10,
      data: [65, 59, 80, 81, 56, 55, 40],
    },
  ],
};

const bar = {
  labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
  datasets: [
    {
      label: 'My First dataset',
      backgroundColor: 'rgba(255,99,132,0.2)',
      borderColor: 'rgba(255,99,132,1)',
      borderWidth: 1,
      hoverBackgroundColor: 'rgba(255,99,132,0.4)',
      hoverBorderColor: 'rgba(255,99,132,1)',
      data: [65, 59, 80, 81, 56, 55, 40],
    },
  ],
};

const options = {
  tooltips: {
    enabled: false,
    custom: CustomTooltips
  },
  maintainAspectRatio: false
};

class CompanyEarning extends Component {

  render() {
    return (
      <div className="animated fadeIn mt-3">
          <Row>
            <Col md = "1" className = "byDateOrWeek">
              <InputGroup>
                <Input type="select">
                  <option>Monthly</option>
                  <option>Weekly</option>
                </Input>
              </InputGroup>
            </Col>
            <Col className = "dateStart">
              <InputGroup>
                <InputGroupAddon addonType="prepend">
                  <InputGroupText>
                    <i className="icon-calendar"></i>
                  </InputGroupText>
                </InputGroupAddon>
                <Input type="date"/>
              </InputGroup>
            </Col>
            
              <Label>-</Label>
            
            <Col className = "dateEnd">
              <InputGroup>
                <InputGroupAddon addonType="prepend">
                  <InputGroupText>
                    <i className="icon-calendar"></i>
                  </InputGroupText>
                </InputGroupAddon>
                <Input type="date"/>
              </InputGroup>
            </Col>
          </Row>
          <Row className = "mt-1">
            <Col md = "6">
              <Card>
                <CardBody>
                  <Table hover bordered responsive className="table-outline mb-0 d-none d-sm-table">
                    <thead className="thead-light">
                    <tr>
                      <th className = "jobtitleHeader">Name(Job Title)</th>
                      <th className = "ageHeader">Age</th>
                      <th>NickName</th>
                      <th className = "employeeHeader">Employee</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                      <td>Vishnu Serghei</td>
                      <td>45</td>
                      <td>Member</td>
                      <td>
                        <Badge color="success">Active</Badge>
                      </td>
                    </tr>
                    <tr>
                      <td>Zbyněk Phoibos</td>
                      <td>37</td>
                      <td>Staff</td>
                      <td>
                        <Badge color="danger">Banned</Badge>
                      </td>
                    </tr>
                    <tr>
                      <td>Einar Randall</td>
                      <td>87</td>
                      <td>Admin</td>
                      <td>
                        <Badge color="secondary">Inactive</Badge>
                      </td>
                    </tr>
                    <tr>
                      <td>Félix Troels</td>
                      <td>69</td>
                      <td>Member</td>
                      <td>
                        <Badge color="warning">Pending</Badge>
                      </td>
                    </tr>
                    <tr>
                      <td>Aulus Agmundr</td>
                      <td>17</td>
                      <td>Staff</td>
                      <td>
                        <Badge color="success">Active</Badge>
                      </td>
                    </tr>
                    
                    </tbody>
                  </Table>
                </CardBody>
              </Card>
            </Col>
            <Col md = "6">
              <Card>
                <CardBody>
                  <div className="chart-wrapper">
                    <Line data={line} options={options} />
                  </div>
                </CardBody>
              </Card>
            </Col>
          </Row>
          <Row className = "mt-1">
            <Col md = "6">
              <Card>
                <CardHeader>
                  Team Ranking Chart
                </CardHeader>
                <CardBody>
                  <div className="chart-wrapper">
                    <Bar data={bar} options={options} />
                  </div>
                </CardBody>
              </Card>
            </Col>
            <Col md = "6">
              <Card>
                <CardHeader>
                  Individual Ranking Chart
                </CardHeader>
                <CardBody>
                  <div className="chart-wrapper">
                    <Bar data={bar} options={options} />
                  </div>
                </CardBody>
              </Card>
            </Col>
          </Row>
      </div>
    );
  }
}

export default CompanyEarning;
