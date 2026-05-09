from django.shortcuts import render

from recipe.models import Recipe


def home(request):
    recipes = Recipe.objects.all().order_by('-created_at')[:3]
    return render(request, 'home.html', {'recipes': recipes})