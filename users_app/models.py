from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_adress = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name},{self.last_name}"
    
    def __repr__(self):
        return f"Name:{self.first_name},  Last_name:{self.last_name}, Email:{self.email_adress}, Age: {self.age}"


# from users_app.models import *
# User.objects.all()
# User.objects.create(first_name="Gustavo", last_name="Lopez",email_address="gustavo@correo.com", age=52)
# User.objects.create(first_name="Rodrigo", last_name="Feliu",email_address="rodrigo@correo.com", age=39)
# User.objects.create(first_name="Carlos", last_name="Rozas",email_address="carlos@correo.com", age=38)
# User.objects.all()
# User.objects.last() 
# User.objects.first() 
# user_for_update = User.objects.get(id=3)
# user_for_update.last_name="Pancakes"
# user_for_update.save()
# Users.objects.get(id=3)
# user_for_delete = Users.objects.get(id=2)
# user_for_delete.delete()
# Users.objects.all().order_by("first_name")
# Users.objects.all().order_by("-first_name")