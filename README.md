# HRMS - Human Resource Management System

This project is a **Human Resource Management System** (HRMS) built with Django, designed to manage employee data, track attendance, and handle related HR functionalities such as adding employees and viewing attendance.

### Main Functionalities

1. **Employee Management**: 
   - View all employees
   - Add a new employee to the system
   - Manage employee details such as first name, last name, department, and salary.

2. **Attendance Tracking**:
   - Mark attendance for employees (present or absent)
   - View attendance records along with employee details (name, department, etc.)

3. **API Endpoints** (using Django REST Framework):
   - Add an employee via API (`/api/add-employee/`)
   - View all employees via API (`/api/get-all-employees/`)
   - Mark attendance via API (`/api/mark-attendance/<employee_id>/`)
   - View attendance records via API (`/api/get-attendance/<employee_id>/`)

## Prerequisites

- **Python** (>= 3.7)
- **Django** (>= 3.0)
- **Django REST Framework** (for API functionality)
- **SQLite** (default database used by Django)




## Installation and Setup


### Step 1: Create and Activate Virtual Environment

Use a virtual environment to manage project dependencies:
Note : Install python, django and restframework 

```powershell
python -m venv env
env/Scripts/activate  # On Mac, use `source env\bin\activate`
```

### Step 2: Set Up the Database

Run migrations to set up the database schema:

```powershell
python manage.py makemigrations
python manage.py migrate
```

### Step 3: Run the Application Locally

Once everything is set up, start the local development server:

```powershell
python manage.py runserver
```

### Step 7: Access the App

- Open your browser and go to `http://127.0.0.1:8000/` to view the app.

## Usage

1. **Add Employees**: Navigate to the "Add Employee" page (`/add_emp`) to create new employee records.
2. **View Employees**: Go to the "View All Employees" page (`/all_emp`) to see the list of all employees in the system.
3. **Attendance Tracking**: Mark and view attendance records of employees by navigating to `/emp-attendance/`.

## API Usage

The project includes API endpoints for interacting with the system and run them in bash shell:

- **Add Employee**: `POST /api/add-employee/`
- **View All Employees**: `GET /api/get-all-employees/`
- **Mark Attendance**: `POST /api/mark-attendance/<employee_id>/`
- **Get Attendance**: `GET /api/get-attendance/<employee_id>/`

## Example Usage

### Python Interactive Shell

``` python
from hrms_project.models import Department, Employee 

# Create Department objects
finance = Department.objects.create(name="Finance")
marketing = Department.objects.create(name="Marketing")
engineering = Department.objects.create(name="Engineering")
hr = Department.objects.create(name="HR")
sales = Department.objects.create(name="Sales")
it = Department.objects.create(name="IT")
legal = Department.objects.create(name="Legal")
operations = Department.objects.create(name="Operations")

# Create Employee objects
Employee.objects.create(first_name="John", last_name="Doe", dept=finance, salary=60000)
Employee.objects.create(first_name="Jane", last_name="Smith", dept=marketing, salary=55000)
Employee.objects.create(first_name="Robert", last_name="Brown", dept=engineering, salary=75000)
Employee.objects.create(first_name="Emily", last_name="Davis", dept=hr, salary=50000)
Employee.objects.create(first_name="Michael", last_name="Johnson", dept=sales, salary=65000)
Employee.objects.create(first_name="Sarah", last_name="Williams", dept=it, salary=70000)
Employee.objects.create(first_name="David", last_name="Jones", dept=legal, salary=80000)
Employee.objects.create(first_name="Emma", last_name="Miller", dept=operations, salary=62000)
Employee.objects.create(first_name="James", last_name="Wilson", dept=finance, salary=58000)
```
### Mark Attendance of Employee 1

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"date":"2024-10-01", "present":true}' \
http://localhost:8000/api/mark-attendance/1/

```
### Get Attendance of Employee 1

```bash
curl -X GET http://localhost:8000/api/get-attendance/1/

```

