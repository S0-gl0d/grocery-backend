from django.db import models
from django.utils import timezone
# Create your models here.


class OrderModel(models.Model):
    contact_bio = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)