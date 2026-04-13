from django.db import models


class Questionnaire(models.Model):

    full_name = models.CharField(max_length=100)

    age = models.IntegerField()

    birth_date = models.DateField()

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    city = models.CharField(max_length=100)

    hobby = models.TextField()

    favorite_subject = models.CharField(max_length=100)

    about_me = models.TextField()

    photo = models.ImageField(upload_to='photos/')

    document = models.FileField(upload_to='documents/')

    def str(self):
        return self.full_name