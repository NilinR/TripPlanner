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


Hotel Booking
:-------------------------:
![image](https://github.com/user-attachments/assets/e3e1d271-0eef-468b-a697-3e8525a86c53)


Report
:-------------------------:
![image](https://github.com/user-attachments/assets/1768073d-bd3d-44c5-8769-a652da757b8a)


Live Chat Support           
:-------------------------:
![live chat support](https://user-images.githubusercontent.com/19711677/86519249-7b86dc00-bdfe-11ea-8809-cb1e7c304637.JPG)

 
Product List Page       |  Product Detail Page
:-------------------------:|:-------------------------:
![shop](https://user-images.githubusercontent.com/19711677/86519337-79714d00-bdff-11ea-88a0-4001d8ab386a.JPG) | ![Product Detail Page](https://user-images.githubusercontent.com/19711677/86519245-7aee4580-bdfe-11ea-802f-154ad56b80ff.JPG)

Checkout Page 
:-------------------------:
![Checkout page](https://user-images.githubusercontent.com/19711677/86519248-7b86dc00-bdfe-11ea-9df0-4b1113de6938.JPG)


PayPal Payment Page
:-------------------------:
![Payment Page](https://user-images.githubusercontent.com/19711677/86519247-7b86dc00-bdfe-11ea-81f5-6a32aa760d7d.JPG)

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
* Python 3
* Javascript
* Jquery 
* Django 1.11
* HTML5
* CSS3 
* Bootstrap 4
* Font awesome
* PostgreSQL
* Celery
* Redis
* Ngrok

## Setup

To run this app, you will need to follow these 3 steps:

#### 1. Requirements
  - a Laptop

  - Text Editor or IDE (eg. vscode, PyCharm)

  - [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed on your Laptop.


#### 2. Install Python and Pipenv
  - [Python3](https://www.python.org/downloads/)
  

  - [Pipenv](https://pipenv-es.readthedocs.io/es/stable/)

#### 3. Local Setup and Running on Windows, Linux and Mac OS

  ```
  # Clone this repository into the directory of your choice
  $ git clone https://github.com/Williano/Final-Senior-Year-Project-.git

  # Move into project folder
  $ cd Final-Senior-Year-Project-

  # Install from Pipfile
  $ pipenv install -r requirements.txt 

  # Activate the Pipenv shell
  $ pipenv shell

  # Create database tables
  (Final-Senior-Year-Project-XXXX) $ python manage.py migrate
  
  # Create superuser account
  (Final-Senior-Year-Project-XXXX) $ python manage.py createsuperuser

  # Start server
  (Final-Senior-Year-Project-XXXX) $ python manage.py runserver
  
  # Copy the IP address provided once your server has completed building the site. (It will say something like >> Serving at 127.0.0.1....).
  
  # Open the address in the browser
  >>> http://127.0.0.1:XXXX
  
  
  # Django Admin
  >>> http://127.0.0.1:XXXX/admin/
  ```


## Contact
Created by [Williano](https://williano.github.io/) - feel free to contact me!

