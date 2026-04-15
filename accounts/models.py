from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    phone = models.CharField(max_length=20)

    age = models.IntegerField(null=True, blank=True)

    city = models.CharField(max_length=100)

    address = models.CharField(max_length=255)

    birth_date = models.DateField(null=True, blank=True)

    gender = models.CharField(max_length=10)

    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    bio = models.TextField(blank=True)

    hobby = models.CharField(max_length=100)

    education = models.CharField(max_length=100)