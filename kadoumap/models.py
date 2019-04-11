from django.db import models


# Create your models here.
class OpeData(models.Model):
    ope_datetime = models.CharField(max_length=19)
    ope_state = models.CharField(max_length=1)
    ope_machine = models.CharField(max_length=10)
