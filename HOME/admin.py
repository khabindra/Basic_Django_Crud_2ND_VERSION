from django.contrib import admin
from .models import Registration
@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','password']