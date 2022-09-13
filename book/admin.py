from secrets import choice
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','category')
    search_fields = ['title']
    list_filter = ('title','category')
admin.site.register(Book,BookAdmin)