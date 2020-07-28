from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from.models import Product


def home(request):
    product = Product.objects.all()
    return render(request, 'home.html', {'product': product})


def new(request):
    return HttpResponse('New Products')
