from django.conf.urls import url
from django.contrib import admin

from .views import(
    team,
)

urlpatterns = [
    url(r'^$', team),
]
