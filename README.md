# Employee RAG System

A Django-based application that retrieves employee information from a PostgreSQL database and generates a context-aware performance summary based on employee work data.

The system allows users to search for an employee using **Employee ID** or **Employee Name**, fetches their information from the database, and generates a structured performance summary.

---

# Features

* Search employees using **Employee ID** or **Employee First Name**
* Retrieve employee personal and work information
* Generate a **context-aware performance summary**
* Admin panel for managing employee records
* REST API built with **Django REST Framework**
* PostgreSQL database integration
* Simple frontend interface for testing the API

---

# Tech Stack

* Python
* Django
* Django REST Framework
* PostgreSQL
* HTML + JavaScript

---

# Project Structure

```
employee_rag_project
│
├── employee_rag_project
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── employees
│   ├── migrations
│   ├── models.py
│   ├── serializers.py
│   ├── services.py
│   ├── views.py
│   └── urls.py
│
├── templates
│   └── home.html
│
└── manage.py
```

---

# Installation Guide

Follow the steps below to run the project on your system.

---

# 1. Clone the Repository

```
git clone <repository-url>
cd employee_rag_project
```

---

# 2. Create a Virtual Environment

Create a virtual environment to isolate project dependencies.

```
python -m venv venv
```

Activate it.

### Windows

```
venv\Scripts\activate
```

### Mac / Linux

```
source venv/bin/activate
```

---

# 3. Install Dependencies

Install required Python packages.

```
pip install django
pip install djangorestframework
pip install psycopg2-binary
```

(Optional)

Create a requirements file:

```
pip freeze > requirements.txt
```

Install dependencies using:

```
pip install -r requirements.txt
```

---

# 4. Install and Setup PostgreSQL

Make sure PostgreSQL is installed on your system.

Create a database:

```
CREATE DATABASE employee_rag_db;
```

Update your **settings.py** database configuration.

Example:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'employee_rag_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

Replace `your_password` with your PostgreSQL password.

---

# 5. Run Database Migrations

Create database tables.

```
python manage.py makemigrations
python manage.py migrate
```

---

# 6. Create Admin Superuser

Create an admin account to manage employee data.

```
python manage.py createsuperuser
```

Enter the following:

```
Username
Email
Password
```

Example:

```
Username: admin
Email: admin@example.com
Password: ********
```

---

# 7. Start the Development Server

Run the server:

```
python manage.py runserver
```

Open the application:

```
http://127.0.0.1:8000/
```

---

# Using the Application

## Home Page

Visit:

```
http://127.0.0.1:8000/
```

Enter:

* Employee Name
  or
* Employee ID

Click **Search** to view:

* Generated performance summary
* Employee details

---

# Admin Panel

Open:

```
http://127.0.0.1:8000/admin/
```

Login using the **superuser credentials**.

From the admin panel you can:

* Add employees
* Add employee work information
* Edit employee records

---

# Inserting Data into the Database

Before testing the application, you need to insert employee data.

---

#  Using Django Admin 

1. Start the server:

```
python manage.py runserver
```

2. Open the admin panel:

```
http://127.0.0.1:8000/admin/
```

3. Login with your superuser credentials.

You will see two models:

* **Employee Details**
* **Employee Work**

---

## Add Employee Details

Example:

```
Employee ID: 101
Employee First Name: Srinij
Employee Last Name: Reddy
Email: srinij@example.com
Phone: 9876543210
```

Click **Save**.

---

## Add Employee Work Information

Example:

```
Work ID: 56
Employee: srinij
Role: Software Engineer
Department: Engineering
Office Location: Hyderabad
Projects: ["AI Tool", "Dashboard"]
Number of Projects Completed: 5
Rating: 4.5
Performance Summary: srinij consistently delivers high quality work and contributes positively to the team.
```

Click **Save**.

---



Now you can search:

```
http://127.0.0.1:8000/employees/employee_query/?query=Alice
```

---

# API Endpoint

Search employee data.

```
GET /employees/employee_query/?query=<value>
```

Example:

```
http://127.0.0.1:8000/employees/employee_query/?query=srinij
```

or

```
http://127.0.0.1:8000/employees/employee_query/?query=EMP101
```

---

# Example API Response

```
{
  "summary": "srinij works as a Software Engineer in the Engineering department located in Hyderabad. The employee has successfully completed 5 projects including AI Tool and Dashboard. Their performance rating is 4.5/5.",

  "employee": {
    "employee_id": "EMP101",
    "employee_first_name": "sriij",
    "employee_last_name": "reddy",
    "email": "srinij@example.com",
    "phone": "9876543210",
    "work": [
      {
        "role": "Software Engineer",
        "department": "Engineering",
        "office_location": "Hyderabad",
        "projects": ["AI Tool", "Dashboard"],
        "no_of_projects_completed": 5,
        "rating": 4.5
      }
    ]
  }
}
```

---

# How the System Works

1. User searches for an employee.
2. Django retrieves employee details from the PostgreSQL database.
3. Work-related information is fetched.
4. A structured context is created using employee data.
5. The system generates a performance summary.
6. The result is returned through the API and displayed on the UI.

---

<img width="1733" height="874" alt="image" src="https://github.com/user-attachments/assets/71a96a00-bffe-43f6-a5c7-771af9f05d34" />


---

# Author

Srinij Reddy Musku
B.Tech CSE (Data Science)
Institute of Aeronautical Engineering
