from django.contrib import admin
from .models import Product,CartItem,Order,OrderItem,Payment, Shipment
from customer.models import Customer
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price')
    search_fields = ['name']
    list_filter = ('name','price')
admin.site.register(Product,ProductAdmin)
admin.site.register(Customer)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Shipment)
admin.site.register(Payment)
# Register your models here.
