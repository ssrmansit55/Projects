from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
import time

class Station(models.Model):
    id = models.IntegerField(primary_key=True, validators=[
        MaxValueValidator(99999999),
        MinValueValidator(10000000)
    ]) # 8 DIGIT ID
    name = models.CharField(max_length=50, default='')
    url_suffix = models.CharField(max_length=70, default='')
    created_at = models.DateTimeField(default=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

    def __unicode__(self):
        return str(self.id) + " : " + self.name

