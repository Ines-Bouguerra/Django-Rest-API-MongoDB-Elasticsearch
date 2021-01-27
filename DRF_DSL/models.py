from django.db import models

# Create your models here.


class University(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Student(models.Model):

    year_in_school = models.CharField(
        max_length=2)
    age = models.SmallIntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
