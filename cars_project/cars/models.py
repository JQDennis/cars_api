from django.db import models

class Cars(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date_added = models.DateField(auto_now=True)