from django.contrib import admin

# Register your models here.
from . models import Portfolio

class PortfolioModelAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'updated']

    class Meta:
        model = Portfolio

admin.site.register(Portfolio, PortfolioModelAdmin)
