from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('rest', views.BookList.as_view()),
    path('rest/<int:pk>',views.BookDetail.as_view())
]