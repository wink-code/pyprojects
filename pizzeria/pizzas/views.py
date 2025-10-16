from django.shortcuts import render, redirect
from .models import Pizza

# Create your views here.
def index(request):
    """The home page for Pizzeria"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """The pizzas page"""
    pizzas = Pizza.objects.all()
    context = {'pizzas':pizzas}
    return render(request, 'pizzas/pizzas.html', context=context)

def pizza(request, pizza_id):
    """The details page for a single pizza"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.toppings.all()
    context = {'pizza':pizza, 'toppings':toppings}
    return render(request, 'pizzas/pizza.html', context=context)

def new_topic(request):
