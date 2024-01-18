# urls.py in the 'recipes' app
from django.urls import path
from .views import home, RecipeListView, RecipeDetailView

app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),  # Assuming you want to use 'home' as the name for the home view
    path('list/', RecipeListView.as_view(), name='list'),
    path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
]
