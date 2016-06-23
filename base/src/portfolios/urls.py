from django.conf.urls import url
from django.contrib import admin

from .views import(
    portfolio,
)

urlpatterns = [
    url(r'^$', portfolio),
]
