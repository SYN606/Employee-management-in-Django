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
        role = request.POST['role']
        
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        

        new_emp = Employee(first_name = first_name, last_name = last_name, dept_id = dept, role_id = role, salary = salary, bonus = bonus, phone = phone, hire_date = datetime.now())

        new_emp.save()

        return HttpResponse("user created")
    else:
        dis_department = Department.objects.all()
        dis_role = Role.objects.all() # for displaying role and department in frontend site.
        context = {
            'dis_dept' : dis_department,
            'dis_role' : dis_role
        }
        return render(request, 'add.html', context)


def remove(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully")
        except:
            return HttpResponse("Something Went Wrong...//")

    return render(request, 'remove.html')


def filter(request):
    return render(request, 'filter.html')