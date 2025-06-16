from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)
    head = models.CharField(max_length=100, blank=True)
    budget = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.location}"


class Employee(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    EMPLOYMENT_TYPE = [
        ('FT', 'Full-time'),
        ('PT', 'Part-time'),
        ('CT', 'Contract'),
        ('IN', 'Intern'),
    ]

    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.BigIntegerField(default=0)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1,
                              choices=GENDER_CHOICES,
                              default='M')
    job_title = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=2,
                                       choices=EMPLOYMENT_TYPE,
                                       default='FT')

    dept = models.ForeignKey(Department,
                             on_delete=models.CASCADE,
                             related_name="employees")
    salary = models.PositiveIntegerField(default=0)
    bonus = models.PositiveIntegerField(default=0)
    hire_date = models.DateField()

    profile_picture = models.ImageField(upload_to='employees/',
                                        null=True,
                                        blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} - {self.job_title}"


class Attendance(models.Model):
    STATUS_CHOICES = [
        ("Present", "Present"),
        ("Absent", "Absent"),
        ("Leave", "Leave"),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default="Present")

    def __str__(self) -> str:
        return f"{self.employee} - {self.date} - {self.status}"


class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    reason = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.employee} Leave from {self.from_date} to {self.to_date}"


class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    review_date = models.DateField()
    rating = models.PositiveIntegerField()
    feedback = models.TextField()

    def __str__(self) -> str:
        return f"{self.employee} - {self.review_date} - Rating: {self.rating}"
