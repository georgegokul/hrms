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
