from django.contrib import admin
from django.urls import path, include
from todoapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('edit/<int:id>/',views.edit,name='edit')
]
