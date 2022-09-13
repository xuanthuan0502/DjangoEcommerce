from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rest', views.rest_Laptop, name='rest'),
    path('rest/<int:pk>',views.laptop_detail)
]