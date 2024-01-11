from django.db import models

# Create your models here.
class Recipe(models.Model):
    difficulty_options=(('easy','Easy'),('medium','Medium'),('intermediate','Intermediate'),('hard','Hard'))

    id = models.FloatField(primary_key=True) 
    name = models.CharField(max_length=100)
    cooking_time = models.FloatField(help_text= 'in minutes')
    ingredients = models.CharField(max_length=250)
    difficulty = models.CharField(max_length =20,choices= difficulty_options, default ='')
    def __str__(self):
        return str(self.name) 