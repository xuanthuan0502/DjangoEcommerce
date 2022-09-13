from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('single-product/<int:pk>', views.single_product, name='single_product'),
    path('orderlist/<int:pk>', views.orderlist, name='orderlist'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('order',views.order,name ='order'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
   # path('checkout', name='signup'),
]