
from django.contrib import admin
from django.urls import path
from HOME.views import Home,Form,Register,show_data,delete_data,edit_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name='home'),
    path('form/',Form,name='form'),
    path('register/',Register,name='register'),
    path('showdata/', show_data, name='showdata'), 
    path('delete/<int:pk>',delete_data,name='delete'),
    path('edit/<int:pk>/', edit_data.as_view(), name='edit'),
]
