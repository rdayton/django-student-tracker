# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^(?P<pk>\d+)/$',
        view=views.select_for_single ,  
        name='select_for_single',
       
    ),
    url(
        regex=r'^basketball/(?P<pk>\d+)/$',
        view=views.basketball ,  
        name='basketball',
       
    ),
    url(
        regex=r'^clean/(?P<pk>\d+)/$',
        view=views.clean ,  
        name='clean',
       
    ),
    url(
        regex=r'^plain/(?P<pk>\d+)/$',
        view=views.plain ,  
        name='plain',
       
    ),
    url(
        regex=r'^multi/$',
        view=views.select_multiple_students ,  
        name='multi',
       
    ),
    url(
        regex=r'^multi/business/$',
        view=views.business ,  
        name='business',
       
    ),
    ]