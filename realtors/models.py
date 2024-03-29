from django.db import models
from datetime import datetime

# Create your models here.

class Realtor(models.Model):
    first = models.CharField()
    last = models.CharField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField()
    email = models.CharField()
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f'{self.first} {self.last}'
