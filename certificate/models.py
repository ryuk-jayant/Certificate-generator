from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class student(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name=models.CharField((""),max_length=20)
    email=models.EmailField((""), max_length=254)
