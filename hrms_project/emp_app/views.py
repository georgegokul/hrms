from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, HttpResponse
from .models import Employee, Department, Attendance
from django.db.models import Q
from .serializers import EmployeeSerializer
from django.shortcuts import render, get_object_or_404
from datetime import date

# Create your views here.
def index(request):
    """
    Renders the home page with a list of employees.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered template displaying employee list.
    """
    employees = Employee.objects.all()
    return render(request, 'index.html', {'employees': employees})


def all_emp(request):
    """
    Renders a page showing all employees.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered template displaying all employees.
        A route handler to display the list of employees on the home page
    """
    emps = Employee.objects.all()
    context = {'emps': emps}
    return render(request, 'view_all_emp.html', context)


def add_emp(request):
    """
    Adds a new employee to the system or renders the form for adding an employee.

    Args:
        request: The HTTP request object (POST for adding an employee, GET for rendering the form).

    Returns:
        HttpResponse: Success message or rendered form.
    """
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        dept = int(request.POST['dept'])
        new_emp = Employee(first_name=first_name, last_name=last_name, salary=salary, dept_id=dept)
        new_emp.save()
        return HttpResponse('Employee added Successfully')
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("An Exception Occurred! Employee Has Not Been Added")


@api_view(['POST'])
def add_employee(request):
    """
    API endpoint to add a new employee.

    Args:
        request: The HTTP request object containing employee data in JSON format.

    Returns:
        Response: JSON data of the newly added employee or error message.
    """
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_employees(request):
    """
    API endpoint to retrieve a list of all employees.

    Args:
        request: The HTTP request object.

    Returns:
        Response: JSON data of all employees.
    """
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def mark_attendance(request, employee_id):
    """
    API endpoint to mark attendance for a specific employee.

    Args:
        request: The HTTP request object containing attendance data (date and present status).
        employee_id: The ID of the employee for whom attendance is being marked.

    Returns:
        Response: Success message or error message.
    """
    try:
        employee = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

    attendance_date = request.data.get('date', str(date.today()))  # default to today if no date is provided
    present = request.data.get('present', True)

    attendance, created = Attendance.objects.update_or_create(
        employee=employee,
        date=attendance_date,
        defaults={'present': present}
    )

    if created:
        return Response({'message': 'Attendance marked'}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message': 'Attendance updated'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_attendance(request, employee_id):
    """
    API endpoint to retrieve attendance details for a specific employee.

    Args:
        request: The HTTP request object.
        employee_id: The ID of the employee whose attendance is being retrieved.

    Returns:
        Response: JSON data of the employee's attendance records or error message.
    """
    try:
        employee = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

    attendances = Attendance.objects.filter(employee=employee).values('date', 'present')
    return Response({'attendances': list(attendances)}, status=status.HTTP_200_OK)


def employee_attendance_detail(request):
    """
    Renders the attendance details page, displaying attendance records for all employees.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered template showing attendance records with employee details.
    """
    attendance_records = Attendance.objects.select_related('employee').all()  # Fetch attendance along with employee info
    return render(request, 'emp_attendance_detail.html', {'attendance_records': attendance_records})
