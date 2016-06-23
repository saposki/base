from django.contrib import admin

# Register your models here.
from . models import Page

class PageModelAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'updated']

    class Meta:
        model = Page

admin.site.register(Page, PageModelAdmin)
