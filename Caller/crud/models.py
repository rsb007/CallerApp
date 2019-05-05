# Create your models here.
from django.db import models


# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=10, unique=False)
    email = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=10, unique=True)
    spam = models.BooleanField(default=False)

    def __str__(self):
        return self.name