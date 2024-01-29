from django import forms

CHART__CHOICES = (          #specify choices as a tuple
   ('#1', 'Bar chart'),    # when user selects "Bar chart", it is stored as "#1"
   ('#2', 'Pie chart'),
   ('#3', 'Line chart')
   )
DIFFICULTY_CHOICES = (
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('intermediate', 'Intermediate'),
    ('hard', 'Hard'),
    ('all', 'Show All Recipes'),
)

class RecipesSearchForm(forms.Form):
    recipes_diff = forms.ChoiceField(choices= DIFFICULTY_CHOICES)
    chart_field = forms.ChoiceField(choices=CHART__CHOICES)