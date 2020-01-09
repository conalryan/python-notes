from django.db import models

# Create your models here.
class posts(models.Model):
    
    author = models.CharField(max_length = 30)
    title = models.CharField(max_length = 100)
    stock = models.CharField(max_length = 6)
    stockPrice = models.DecimalField(max_digits=6, decimal_places=2)
    bodyText = models.TextField()
    timeStamp = models.DateTimeField()