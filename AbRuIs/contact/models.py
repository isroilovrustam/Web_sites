from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
