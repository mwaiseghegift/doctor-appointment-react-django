// AppointmentsForm.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';

const AppointmentsForm = () => {
  const [department, setDepartment] = useState('');
  const [doctor, setDoctor] = useState('');
  const [name, setName] = useState('');
  const [date, setDate] = useState('');
  const [time, setTime] = useState('');
  const [email, setEmail] = useState('');
  const [phoneNo, setPhoneNo] = useState('');
  const [message, setMessage] = useState('');

  const [departments, setDepartments] = useState([]); // Updated variable name to "departments"
  const [doctors, setDoctors] = useState([]); // Updated variable name to "doctors"

  useEffect(() => {
    axios
      .get('http://localhost:8000/api/departments/')
      .then((res) => {
        console.log(res.data);
        setDepartments(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);

  useEffect(() => {
    axios
      .get('http://localhost:8000/api/doctors/')
      .then((res) => {
        console.log(res.data);
        setDoctors(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    const appointment = {
      department : parseInt(department),
      doctor : parseInt(doctor),
      name,
      date,
      time,
      email,
      phoneNo,
      message,
    };
    axios
      .post('http://localhost:8000/api/add-appoinment/', appointment)
      .then((res) => {
        console.log(res.data);
        alert('Appointment booked successfully');
      })
      .catch((err) => {
        console.log(err);
      });
  };



  return (
    <div>
      <h1>Appointment Form</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Department:
          <select value={department} onChange={(e) => setDepartment(e.target.value)}>
            {departments.map((dept) => ( // Updated variable name to "dept"
              <option key={dept.id} value={dept.id}>
                {dept.name}
              </option>
            ))}
          </select>

        </label>
        <br />
        <label>
          Doctor:
          <select value={doctor} onChange={(e) => setDoctor(e.target.value)}>
            {doctors.map((doc) => ( // Updated variable name to "doc"
              <option key={doc.id} value={doc.id}>
                {doc.name}
              </option>
            ))}
          </select>
          
        </label>
        <br />
        <label>
          Name:
          <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
        </label>
        <br />
        <label>
          Date:
          <input type="date" value={date} onChange={(e) => setDate(e.target.value)} />
        </label>
        <br />
        <label>
          Time:
          <input type="time" value={time} onChange={(e) => setTime(e.target.value)} />
        </label>
        <br />
        <label>
          Email:
          <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} />
        </label>
        <br />
        <label>
          Phone No:
          <input type="text" value={phoneNo} onChange={(e) => setPhoneNo(e.target.value)} />
        </label>
        <br />
        <label>
          Message:
          <textarea value={message} onChange={(e) => setMessage(e.target.value)} />
        </label>
        <br />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default AppointmentsForm;
