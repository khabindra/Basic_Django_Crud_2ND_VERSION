from django.db import models

# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=30, default="example@example.com")
    password = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    