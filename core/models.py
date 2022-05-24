from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Boiler(models.Model):
    objects = None
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    id = models.AutoField(primary_key=True)
    Course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now=True, null=True)
    updated = models.DateTimeField(auto_now_add=True, null=True)

    # class Meta:
    #     ordering = ['-updated', '-created']

    def __str__(self):
        return self.id
