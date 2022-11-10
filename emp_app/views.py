from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime

def index(request):
    return render(request, 'index.html')
    

def view(request):
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render(request, 'view.html', context)



def add(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = request.POST['dept']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = request.POST['role']
        phone = int(request.POST['phone'])
        
        hire_date = 0

        if hire_date == None:
            hire_date = datetime.now()
        else:
            hire_date = int(request.POST['hire_date'])

        new_emp = Employee(first_name = first_name, last_name = last_name, dept_id = dept, role_id = role, salary = salary, bonus = bonus, phone = phone, hire_date = hire_date)

        new_emp.save()

        return HttpResponse("user created")
    else:
        return render(request, 'add.html')


def filter(request):
    return render(request, 'filter.html')

def remove(request):
    return render(request, 'remove.html')