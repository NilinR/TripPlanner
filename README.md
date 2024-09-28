![image](https://github.com/user-attachments/assets/bf6b125d-5ae9-4b29-b301-73e795c7e352)

# Trip Planner
Travel Management System built using Python's Tkinter and MySQL database

## Table of contents
* [General info](#general-info)
* [Working](#working)
* [Features](#features)
* [Technologies](#technologies)
* [Setup](#setup)
* [Contact](#contact)

## General info
Trip Planner is a Travel management system built with Python and MySQL as my final 12th grade Python project.

It provides functionalities to book a flight and hotel in one system making the travel booking process easier.

* The system requires a login whos data is stored using python files, 
* GUI display and buttons using tkinter 
* and stores the full booking of flights using MySQL connect.


## Working

Login
:-------------------------:
![login](https://github.com/user-attachments/assets/3ad6c931-5267-4e90-82d3-43566bc7541f)

 Sign Up has restraints for 10 digit contact number and verifies the reentered password.
 
 It stores the username and password in files as nested lists : [[Username,Pass], [Nilin,Nil],]
 
 When Loging in the username is searched for in the file and password is verified.
 
 Finally the login sign is replaced by the username.


Book Flight
:-------------------------:
![image](https://github.com/user-attachments/assets/19e2c512-f079-4187-921e-8000c77abd36)
![image](https://github.com/user-attachments/assets/a59aa472-0de7-45cd-8ae8-00c63a48e48b)

 Enter date into a calander that is verified by current date
 
 Flight distance save in mysql table accessed
 
 Flight cost calculated using distance, avg cost and random module for increments
 
 MySql also verified to make sure only 5 bookings at a time
 
 (Gives fully booked error on 6 flight booked)
 
 Displays a bill as well.
 
Hotel Booking
:-------------------------:
![image](https://github.com/user-attachments/assets/e3e1d271-0eef-468b-a697-3e8525a86c53)


End Report
:-------------------------:
![image](https://github.com/user-attachments/assets/1768073d-bd3d-44c5-8769-a652da757b8a)

## Features

* Multi-language support (10 international language)
* PayPal payment
* Customer Dashboard
* Owner Dashboard
* Google Analytics
* Product Reviews
* Product Recommendations
* Ad support
* Live Chat Support

## Technologies
* Done in Python version 3
* Tkinter GUI
* Python + MySQL connector

## Setup

The modules that are required are:

#### 1. Requirements
  - a Laptop

  - Text Editor or IDE (I used IDLE)


#### 2. Install Python modules
Libraries used:
  -  tkinter
 
  -  datetime
 
  -  tkcalendar
 
  -  math
 
  -  random
 
  -  mysql.connector
 
  -  PIL

to install the libraries (math and random are default):

   py -m pip install [options] <requirement specifier> [library] ...

## Contact
Created by [Nilin Rose](https://github.com/NilinR) nilinr0@gmail.com

