from django.urls import path
from django.contrib import admin
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path("add_task",views.add_task, name="add_task")
]
