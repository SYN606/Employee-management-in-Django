from datetime import datetime
from django.shortcuts import render, redirect
from .models import Department, Employee
from django.contrib import messages
from django.db.models import Q


def index(request):
    data = {"title": "Homepage"}
    return render(request, "index.html", data)


def view(request):
    emps = Employee.objects.all()
    data = {"emps": emps, "title": "View all Employees"}
    return render(request, "view.html", data)


def add(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        dept = request.POST["dept"]
        salary = int(request.POST["salary"])
        bonus = int(request.POST["bonus"])
        phone = int(request.POST["phone"])

        new_emp = Employee(
            first_name=first_name,
            last_name=last_name,
            dept_id=dept,
            salary=salary,
            bonus=bonus,
            phone=phone,
            hire_date=datetime.now(),
        )
        new_emp.save()
        messages.success(request, "Employee Added Successfully")
        return redirect("view")
    else:
        dis_department = (
            Department.objects.all()
        )  # for displaying department in frontend site.
        data = {"dis_dept": dis_department, 'title' : 'Add an Employee'}
        return render(request, "add.html", data)


def remove(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            messages.success(request, "Employee Removed Successfully")
            return redirect("view")
        except:
            messages.warning(request, "Something went wrong.")
            return redirect("view")


def filter(request):
    if request.method == "POST":
        name = request.POST["name"]
        dept = request.POST["dept"]
        emps = Employee.objects.all()

        if name:
            emps = emps.filter(
                Q(first_name__icontains=name) | Q(last_name__icontains=name)
            )
        if dept:
            emps = emps.filter(dept__name__icontains=dept)

        data = {"emps": emps, "title": "Filter employees"}

        return render(request, "view.html", data)

    else:
        data = {"title": "Filter employees"}
        return render(request, "filter.html", data)
