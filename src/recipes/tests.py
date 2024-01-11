from django.test import TestCase
from .models import Recipe

# Create your tests here.

class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(id='1',name='Cake',cooking_time='56',ingredients='flour,milk,vanilla,sugar,eggs',difficulty='hard' )

    def test_recipe_name(self):
        recipe=Recipe.objects.get(id=1)

        field_label = recipe._meta.get_field('name').verbose_name
        self.assertEqual(field_label,'name')
    
    def test_ingredients_max_length(self):
        recipe=Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('ingredients').max_length
        self.assertEqual(max_length, 250)

    def test_cooking_time_is_number(self):
        recipe=Recipe.objects.get(id=1)
        self.assertIsInstance(recipe.cooking_time, (int, float))
