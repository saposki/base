from django.conf.urls import url
from django.contrib import admin

from . views import(
    page,
)

urlpatterns = [
    url(r'^$', page, name='he' ),
]
