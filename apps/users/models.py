# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from tinymce.models import HTMLField

class Project(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(null=True, blank=True)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.title


class Hobby(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Quote(models.Model):
    quote = models.CharField(max_length=150)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.quote


class Activity(models.Model):
    name = models.CharField(max_length=30, default="Not Available")
    description = models.CharField(max_length=150, default="Not Available")
    approved = models.BooleanField(default=False)
    def __str__(self):              # __unicode__ on Python 2
        return self.name


class MiscAccomplishment(models.Model):
    description = models.CharField(max_length=200)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.description


class Competition(models.Model):
    description = models.CharField(max_length=200)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.description


class AreaOfInterest(models.Model):
    description = models.CharField(max_length=200)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.description


class FuturePlan(models.Model):
    description = models.CharField(max_length=200)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.description


class MagnetProgram(models.Model):
    description = models.CharField(max_length=30)
    pathway = models.CharField(max_length=30, default="Not Available")
    
    def __str__(self):              # __unicode__ on Python 2
        return self.description


class School(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=30)
    zip = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    website = models.CharField(max_length=30)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Employer(models.Model):
    name = models.CharField(max_length=140)
    address = models.CharField(max_length=140, null=True, blank=True)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)    
    employer = models.ForeignKey(Employer)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.first_name + " " + self.last_name


class Review(models.Model):
    description = models.CharField(max_length=140)
    reviewer = models.ForeignKey(Employee)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.description


class Task(models.Model):
    description = models.CharField(max_length=240)
    employer = models.ForeignKey(Employer)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.description


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

class Student(models.Model):
    student_id = models.CharField(max_length=10, null=True) 
    user = models.OneToOneField(User, primary_key=True)   
    school = models.ForeignKey(School, null=True)
    magnet_program = models.ForeignKey(MagnetProgram, null=True, blank=True)
    major = models.CharField(max_length=30, null=True, blank=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    grade_level = models.IntegerField()
    projects = models.ManyToManyField(Project, blank=True)
    activities = models.ManyToManyField(Activity, blank=True)
    hobbies = models.ManyToManyField(Hobby, blank=True)
    quotes = models.ManyToManyField(Quote, blank=True)
    competitions = models.ManyToManyField(Competition, blank=True)
    accomplishments = models.ManyToManyField(MiscAccomplishment, blank=True)
    areas_of_interest = models.ManyToManyField(AreaOfInterest, blank=True)
    future_plans = models.ManyToManyField(FuturePlan, blank=True)
    employers = models.ManyToManyField(Employer, blank=True)
    reviews = models.ManyToManyField(Review, blank=True)
    tasks = models.ManyToManyField(Task, blank=True)   
    story = HTMLField(blank=True,null=True)
    def __str__(self):
        return self.user.username
    
    @staticmethod
    def get_search_results(**kwargs ):
        query = Student.objects.all()
        if kwargs.get('gpa'):            
            query = query.filter(gpa__gte = kwargs.get('gpa'))
        if kwargs.get('major'):  
            query = query.filter(major__icontains=kwargs.get('major'))
            
        return query

    @staticmethod
    def get_students_by_ids(ids):
        students = []
        for id in ids:
            students.append(Student.objects.get(pk=id))
        return students