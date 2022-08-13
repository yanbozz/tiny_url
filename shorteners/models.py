from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Url(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    long_url = models.TextField()
    short_url = models.CharField(max_length=100, unique=True, db_index=True)






