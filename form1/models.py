from django.db import models


class contact_form(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField(max_length=200)
    message = models.CharField(max_length=200)
