from django.contrib import admin

from .models import *
@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'species','gender', 'phone')
    search_fields = ['name']
admin.site.register(Species)
admin.site.register(Gender)
admin.site.register(Lost)
