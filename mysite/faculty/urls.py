from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^$', views.faculty_index, name='faculty_index'),
    url('add', views.faculty_add, name='faculty_add'),
    url('NewCafedra', views.faculty_NewCafedra, name='faculty_NewCafedra'),

]