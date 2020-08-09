from django.shortcuts import render

# Create your views here.

def portfolio(request):
    """ Portfolio page view """
    return render(request, 'portfolio/portfolio.html')