from django.contrib import admin
from .models import Portfolio

# Register your models here.

class PortfolioAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'technology',
        'image',
        'demo_url',
    )


admin.site.register(Portfolio, PortfolioAdmin)