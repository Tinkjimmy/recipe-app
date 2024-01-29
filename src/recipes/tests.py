from django.test import TestCase
from django.urls import reverse
from .models import Recipe
from .forms import RecipesSearchForm
from django.contrib.auth.models import User

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

class RecipeViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        Recipe.objects.create(
            id='1',
            name='Cake',
            cooking_time='56',
            ingredients='flour,milk,vanilla,sugar,eggs',
            difficulty='hard',
        )

    

    

    def test_recipe_detail_view_status_code(self):
        recipe = Recipe.objects.get(id=1)
        response = self.client.get(reverse('recipes:detail', kwargs={'pk': recipe.pk}))
        self.assertEqual(response.status_code, 200)

    def test_recipe_detail_view_uses_correct_template(self):
        recipe = Recipe.objects.get(id=1)
        response = self.client.get(reverse('recipes:detail', kwargs={'pk': recipe.pk}))
        self.assertTemplateUsed(response, 'recipes/detail.html')

class RecipeFormTest(TestCase):
    def setUp(self):
        Recipe.objects.create(
            id='1',
            name='Cake',
            cooking_time='56',
            ingredients='flour,milk,vanilla,sugar,eggs',
            difficulty='hard',
        )

    def test_records_view_with_post_status_code(self):
        data = {'recipes_diff': 'all', 'chart_field': '#1'}
        response = self.client.post(reverse('recipes:records'), data)
        self.assertEqual(response.status_code, 200)

    def test_records_view_no_post_status_code(self):
        response = self.client.post(reverse('recipes:records'))
        self.assertEqual(response.status_code, 200)

    def test_records_view_with_filter_status_code(self):
        data = {'recipes_diff': 'easy', 'chart_field': '#1'}
        response = self.client.post(reverse('recipes:records'), data)
        self.assertEqual(response.status_code, 200)

    def test_records_view_uses_correct_template(self):
        response = self.client.get(reverse('recipes:records'))
        self.assertTemplateUsed(response, 'recipes/records.html')

    def test_records_view_contains_form(self):
        response = self.client.get(reverse('recipes:records'))
        self.assertTrue('form' in response.context)
        self.assertIsInstance(response.context['form'], RecipesSearchForm)

    def test_records_view_contains_chart(self):
        response = self.client.get(reverse('recipes:records'))
        self.assertTrue('chart' in response.context)