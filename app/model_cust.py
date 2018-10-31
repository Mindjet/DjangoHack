from django.contrib import admin


class HeroInList(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'affiliation', 'base_of_operation')
