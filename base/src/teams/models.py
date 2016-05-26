from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Team(models.Model):
    #logo
    image = models.ImageField(upload_to='updload_location',
        null=True, blank=True,
        width_field='width_field',
        height_field='height_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    #first name
    first_name = models.CharField(max_length=120, default='title')

    #last name
    last_name = models.CharField(max_length=120, default='title')

    #job title
    last_name = models.CharField(max_length=120, default='title')

    #description
    description = models.TextField(max_length=240, default='description')

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
