from django.db import models

# Create your models here.
class PhoneInfo(models.Model):
    name = models.CharField(max_length=32)
    mobilephone = models.CharField(max_length=128,null=True)
    other_contact = models.CharField(max_length=128,null=True)
    other_contact2 = models.CharField(max_length=128,null=True)
    memo = models.CharField(max_length=256,null=True)
