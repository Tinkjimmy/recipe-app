from django.db import models
from django.urls import reverse

# Create your models here.
class Recipe(models.Model):
    difficulty_options=(('easy','Easy'),('medium','Medium'),('intermediate','Intermediate'),('hard','Hard'))

    id = models.FloatField(primary_key=True) 
    name = models.CharField(max_length=100)
    cooking_time = models.FloatField(help_text= 'in minutes')
    ingredients = models.CharField(max_length=250)
    difficulty = models.CharField(max_length =20,choices= difficulty_options, default ='')
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def __str__(self):
        return str(self.name) 
    def get_absolute_url (self):
        return reverse ('recipes:detail', kwargs={'pk': self.pk})
    @property
    def url(self):
        return reverse('recipes:detail', kwargs={'pk': self.pk})