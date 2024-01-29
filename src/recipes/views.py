from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView,DetailView
from.models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin #this libary is required to protect a class-based view
from .forms import RecipesSearchForm
import pandas as pd
from .utils import get_chart



# Create your views here.
 
def home(request):
    return render(request,'recipes/recipes_home.html')

class RecipeListView(LoginRequiredMixin,ListView):          
   model = Recipe                        
   template_name = 'recipes/main.html' 

class RecipeDetailView(DetailView):
   model = Recipe
   template_name = 'recipes/detail.html'
   

def records(request):
   form = RecipesSearchForm(request.POST or None)
   recipes_df = None #inztialize dataframe to none
   recipes_diff = None
   chart = None
   chart_field = None
   all_recipes = Recipe.objects.none()
    #check if button is clicked
   if request.method == 'POST' and request.POST.get('recipes_diff') == "all":
      qs=Recipe.objects.all()            # show all recipes
     

   else:
      #READ recipe_diff anc chart_type
      recipes_diff = request.POST.get('recipes_diff')
      chart_field = request.POST.get('chart_field')
      qs =Recipe.objects.filter(difficulty=recipes_diff)
   
      
   if qs:
      all_recipes=Recipe.objects.all()

      recipes_df = pd.DataFrame(qs.values())
      recipes_df['url'] = recipes_df.apply(lambda row: reverse("recipes:detail", kwargs={"pk": row["id"]}), axis=1)
      recipes_dict_list = recipes_df.to_dict(orient='records')

      #creating data for the charts
      total_recipes = all_recipes.count()
      total_recipes_dict_list = len(recipes_dict_list)

      rest_of_the_recipes= total_recipes -total_recipes_dict_list
      custom_labels = [recipes_diff, 'Other Difficulties']

      chart =get_chart(chart_field, recipes_df,total_recipes_dict_list,rest_of_the_recipes, labels=custom_labels,)


   else:
      recipes_dict_list =None
      # Pack up data to be sent to the template in the context dictionary
  
   context = {
      'form': form,
      'recipes_df': recipes_dict_list,
      'chart': chart,
   }
   return render(request, 'recipes/records.html',context)