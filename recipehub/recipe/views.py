from django.shortcuts import render,redirect
from .forms import RecipeForm
from .models import Recipe


def view_recipe(request):
    recipes = Recipe.objects.all()
    return render(request, 'all_recipe.html', {'recipes': recipes})

def create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_recipe')
    else:
        form = RecipeForm()
    return render(request, 'forms.html', {'form': form})

def update(request, pk):
    product = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST,request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('view_recipe')
    else:
        form = RecipeForm(instance=product)
    return render(request, 'forms.html', {'form': form})

def delete(request, pk):
    Recipe.objects.get(pk=pk).delete()
    return redirect('view_recipe')
