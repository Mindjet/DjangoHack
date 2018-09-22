from django.contrib import admin
from .models import Hero


class HeroInList(admin.ModelAdmin):
    list_display = ('name', 'position')