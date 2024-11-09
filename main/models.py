from django.db import models

class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Resume(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

class Skill(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.IntegerField(help_text="Enter a percentage (0-100)")

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(null=True, blank=True)

class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=15)
