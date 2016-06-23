from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from . models import Team

def team(request):
    context = {

    }
    return render(request, 'team.html', context)
