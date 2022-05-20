from django.db import models

# Create your models here.
class MediaInfo(models.Model):
    # id = models.IntegerField()
    app_name = models.CharField(max_length=256)
    account = models.CharField(max_length=64)
    passwd = models.CharField(max_length=64)


