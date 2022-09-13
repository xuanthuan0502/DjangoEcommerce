from secrets import choice
from django.contrib import admin
from .models import MobilePhone

#class MobilePhoneAdmin(admin.ModelAdmin):
 #   list_display = ('name','code')
  #  search_fields = ['name']
   # list_filter = ('name','code')
#admin.site.register(MobilePhone,MobilePhoneAdmin)
admin.site.register(MobilePhone)