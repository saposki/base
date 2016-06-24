from __future__ import unicode_literals
from django.core.urlresolvers import reverse


from django.db import models

# Create your models here.
class Contact(models.Model):
    #name
    name = models.CharField(max_length=120, default='name')

    #telephone
    telephone = models.CharField(max_length=120, default='telephone')

    #email
    email = models.CharField(max_length=120, default='email')

    #message
    message = models.TextField(max_length=240, default='message')

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('co', kwargs={})
