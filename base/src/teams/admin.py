from django.contrib import admin

# Register your models here.
from . models import Team

class TeamModelAdmin(admin.ModelAdmin):
    list_display = ['timestamp', 'updated']

    class Meta:
        model = Team

admin.site.register(Team, TeamModelAdmin)
