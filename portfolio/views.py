from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Portfolio

# Create your views here.

def portfolio(request):
    """ Portfolio page view """
    portfolio = Portfolio.objects.all()
    context = {
    'portfolio': portfolio
    }
    return render(request, 'portfolio/portfolio.html', context)