from secrets import choice
from django.contrib import admin
from .models import Laptop

class LaptopAdmin(admin.ModelAdmin):
    list_display = ('name','code')
    search_fields = ['name']
    list_filter = ('name','code')
admin.site.register(Laptop,LaptopAdmin)

# Register your models here.