from django.db import models

# Create your models here.
class User(models.Model):
    id = models.FloatField(primary_key=True) 
    username =models.CharField(max_length=100)
    email = models.EmailField(max_length=254, blank=True, null=True)
    
    def __str__(self):
        return str(self.name)  

