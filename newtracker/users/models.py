# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save

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
    #student_id = models.CharField(max_length=10) 
    user = models.OneToOneField(User, primary_key=True)   
    #school = models.ForeignKey(School)
    #magnet_program = models.ForeignKey(MagnetProgram, null=True, blank=True)
    major = models.CharField(max_length=30, null=True, blank=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2)
    grade_level = models.IntegerField()
    #projects = models.ManyToManyField(Project, blank=True)
    #activities = models.ManyToManyField(Activity, blank=True)
    #hobbies = models.ManyToManyField(Hobby, blank=True)
    #quote = models.ManyToManyField(Quote, blank=True)
    #competitions = models.ManyToManyField(Competition, blank=True)
    #accomplishments = models.ManyToManyField(MiscAccomplishment, blank=True)
    #areas_of_interest = models.ManyToManyField(AreaOfInterest, blank=True)
    #future_plans = models.ManyToManyField(FuturePlan, blank=True)
    #employer = models.ManyToManyField(Employer, blank=True)
    #reviews = models.ManyToManyField(Review, blank=True)
    #tasks = models.ManyToManyField(Task, blank=True)   
    #story = HTMLField(blank=True,null=True)
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