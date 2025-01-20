from django.db import models
import uuid

class UserModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False)
    email = models.EmailField(max_length=200, null=False)
    ph_number = models.CharField(max_length=13, null=False)
    password = models.CharField(max_length=200,null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    address= models.CharField(max_length=200, null=False)

    class Meta:
        db_table = 'User'