from django.db import models

# Create your models here.

class maff(models.Model):
    funk=models.CharField(max_length=10)
    int1=models.FloatField()
    int2 = models.FloatField()

