from django.db import models

# Create your models here.

class Number(models.Model) :
    
    name = models.CharField(max_length=1000000)
    img = models.ImageField(upload_to='pics')
    desc  = models.TextField()
    anke = models.IntegerField() 
    offer  = models.BooleanField(default=False)
    

    
