from django.contrib import admin
from .model_cust import HeroInList
from .models import Hero
# Register your models here.

admin.site.register(Hero, HeroInList)
# admin.site.register([Hero])