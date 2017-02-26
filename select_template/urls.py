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
    ]