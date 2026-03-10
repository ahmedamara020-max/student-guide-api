from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    full_name = models.CharField(max_length=255)
    university_id = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password_hash = models.CharField(max_length=255)
    academic_year = models.CharField(max_length=50)
    current_cgpa = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    total_credits = models.IntegerField(default=0)
    cover_image_url = models.CharField(max_length=255, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    subjects = models.ManyToManyField('Subject', related_name='students', blank=True)

    def __str__(self):
        return self.full_name



class Subject(models.Model):
    name = models.CharField(max_length=255)
    credits = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    type = models.CharField(max_length=50) # Lecture or Lab
    hall_location = models.CharField(max_length=100)
    day_of_week = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.subject.name} - {self.type}"


class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam_date = models.DateTimeField()

    def __str__(self):
        return f"{self.subject.name} Exam"


class Todo(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name
    
