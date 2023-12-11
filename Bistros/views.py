from django.shortcuts import render
from Meals.models import Meal


def index(request):
    return render(request, 'index.html')

def menu(request):
    try:
        lunch = Meal.objects.get(Type='Lunch')
        context = {
            'lunch': lunch.Dishes.all()
        }
    except Meal.DoesNotExist:
        context = {
            
        }
    return render(request, 'menu.html', context)
