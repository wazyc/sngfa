from django.db import models


# Create your models here.
class OpeData(models.Model):
    ope_date = models.CharField(max_length=10)
    ope_time = models.CharField(max_length=8)
    ope_state = models.CharField(max_length=1)
    ope_machine = models.CharField(max_length=10)
