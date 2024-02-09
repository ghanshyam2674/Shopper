from django.db import models

# Create your models here.


class User(models.Model):
    user_username = models.CharField(max_length=50)
    user_firstname = models.CharField(max_length=50)
    user_lastname = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=254)
    user_password = models.IntegerField()
    user_address = models.TextField()
