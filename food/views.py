from django.shortcuts import redirect, render
from food.forms import FoodForm
from .models import Food

# Create your views here.

def list(request):
    foodItems = Food.objects.all()
    context = {
        'foodItems': foodItems,
    }
    return render(request, 'food/list.html', context)    

def detail(request, food_id):
    food = Food.objects.get(pk=food_id)
    context = {
        'food': food,
    }
    return render(request, 'food/detail.html', context)

def add(request):
    form = FoodForm(request.POST or None)

    if form.is_valid():
        form.save()        
        return redirect('food:list')

    return render(request, 'food/add.html', {'form': form})

def update(request, food_id):
    food = Food.objects.get(pk=food_id)
    form = FoodForm(request.POST or None, instance=food)

    if form.is_valid():
        form.save()        
        return redirect('food:list')

    return render(request, 'food/add.html', {'form': form, 'food': food })

def delete(request, food_id):
    food = Food.objects.get(pk=food_id)

    if request.method == 'POST':
        food.delete()
        return redirect('food:list')
        
    return render(request, 'food/delete.html', {'food': food }) 

