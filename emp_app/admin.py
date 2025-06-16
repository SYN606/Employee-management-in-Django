from django.contrib import admin
from .models import Employee, Department, Attendance, Leave, Performance


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "location", "head", "budget", "created_at")
    search_fields = ("name", "location", "head")
    ordering = ("name", )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "job_title",
                    "dept", "employment_type", "salary", "phone", "hire_date")
    search_fields = ("first_name", "last_name", "email", "phone", "job_title")
    list_filter = ("dept", "employment_type", "gender", "hire_date")
    ordering = ("-hire_date", )
    date_hierarchy = "hire_date"

    fieldsets = (
        ("Basic Info", {
            "fields": ("first_name", "last_name", "gender", "dob", "email",
                       "phone", "profile_picture")
        }),
        ("Employment Details", {
            "fields": ("job_title", "employment_type", "dept", "hire_date")
        }),
        ("Compensation", {
            "fields": ("salary", "bonus")
        }),
    )


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("employee", "date", "status")
    list_filter = ("status", "date")
    search_fields = ("employee__first_name", "employee__last_name")
    date_hierarchy = "date"
    ordering = ("-date", )


@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ("employee", "from_date", "to_date", "approved")
    list_filter = ("approved", "from_date", "to_date")
    search_fields = ("employee__first_name", "employee__last_name", "reason")
    date_hierarchy = "from_date"
    ordering = ("-from_date", )


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ("employee", "review_date", "rating")
    list_filter = ("rating", "review_date")
    search_fields = ("employee__first_name", "employee__last_name", "feedback")
    ordering = ("-review_date", )
    date_hierarchy = "review_date"
