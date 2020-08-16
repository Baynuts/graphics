from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from products.models import Product, Category

# Create your views here.

def index(request):
    """ Index page view """
    return render(request, 'home/index.html')
