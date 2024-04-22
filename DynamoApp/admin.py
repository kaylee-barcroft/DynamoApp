from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(SingleOrigin)
admin.site.register(Plan)
admin.site.register(Subscription)