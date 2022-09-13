from secrets import choice
from django.contrib import admin
from .models import Clothes

class ClothesAdmin(admin.ModelAdmin):
    list_display = ('type','brand')
    search_fields = ['type']
    list_filter = ('type','brand')
admin.site.register(Clothes,ClothesAdmin)