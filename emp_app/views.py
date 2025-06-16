from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Department, Employee


def index(request):
    """Homepage view"""
    return render(request, "index.html", {"title": "Homepage"})


def view(request):
    """View all employees with detailed fields"""
    employees = Employee.objects.select_related("dept").all().order_by(
        "-hire_date")
    return render(request, "view.html", {
        "emps": employees,
        "title": "Employee Directory"
    })


def add(request):
    """Add a new employee via form POST"""
    departments = Department.objects.all()

    if request.method == "POST":
        # Get and clean form data
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        email = request.POST.get("email", "").strip()
        dob = request.POST.get("dob", "").strip()
        gender = request.POST.get("gender", "").strip()
        phone = request.POST.get("phone", "0")
        dept_id = request.POST.get("dept", "")
        salary = request.POST.get("salary", "0")
        bonus = request.POST.get("bonus", "0")
        job_title = request.POST.get("job_title", "").strip()
        employment_type = request.POST.get("employment_type", "").strip()
        profile_picture = request.FILES.get("profile_picture", None)

        # Validate required fields
        if not first_name or not dept_id:
            messages.error(request, "First Name and Department are required.")
            return render(
                request, "add.html", {
                    "departments": departments,
                    "title": "Add an Employee",
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email,
                    "dob": dob,
                    "gender": gender,
                    "phone": phone,
                    "dept": dept_id,
                    "salary": salary,
                    "bonus": bonus,
                    "job_title": job_title,
                    "employment_type": employment_type,
                })

        try:
            # Convert numeric and date values
            salary = int(salary)
            bonus = int(bonus)
            phone = int(phone)
            dob_date = datetime.strptime(dob,
                                         "%Y-%m-%d").date() if dob else None

            # Create new employee
            Employee.objects.create(first_name=first_name,
                                    last_name=last_name,
                                    email=email,
                                    dob=dob_date,
                                    gender=gender,
                                    phone=phone,
                                    dept_id=dept_id,
                                    salary=salary,
                                    bonus=bonus,
                                    job_title=job_title,
                                    employment_type=employment_type,
                                    hire_date=datetime.now().date(),
                                    profile_picture=profile_picture)

            messages.success(request, "Employee added successfully.")
            return redirect("view")

        except Exception as e:
            messages.error(request, f"Error adding employee: {str(e)}")
            return render(
                request, "add.html", {
                    "departments": departments,
                    "title": "Add an Employee",
                    "first_name": first_name,
                    "last_name": last_name,
                    "email": email,
                    "dob": dob,
                    "gender": gender,
                    "phone": phone,
                    "dept": dept_id,
                    "salary": salary,
                    "bonus": bonus,
                    "job_title": job_title,
                    "employment_type": employment_type,
                })

    else:
        return render(request, "add.html", {
            "departments": departments,
            "title": "Add an Employee"
        })


def remove(request, emp_id=0):
    """Remove an employee by their ID"""
    if emp_id:
        employee = get_object_or_404(Employee, id=emp_id)
        employee.delete()
        messages.success(request, "Employee removed successfully.")
    else:
        messages.warning(request, "Invalid employee ID.")
    return redirect("view")


def filter(request):
    """Filter employees by name, department, or job title"""
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        dept = request.POST.get("dept", "").strip()
        job = request.POST.get("job_title", "").strip()

        emps = Employee.objects.select_related("dept").all()

        if name:
            emps = emps.filter(
                Q(first_name__icontains=name) | Q(last_name__icontains=name))

        if dept:
            emps = emps.filter(dept__name__icontains=dept)

        if job:
            emps = emps.filter(job_title__icontains=job)

        return render(request, "view.html", {
            "emps": emps,
            "title": "Filtered Employees"
        })

    return render(request, "filter.html", {"title": "Filter Employees"})
