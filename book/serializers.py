from curses import meta
from .models import Book
from rest_framework import serializers

#class LaptopSerializer(serializers.Serializer):
 #   name = serializers.CharField(max_length=200)
  #  code = serializers.CharField(max_length=200)
    

class BookSerializer(serializers.ModelSerializer):
    #name = serializers.CharField(max_length=200)
    #code = serializers.CharField(max_length=200)
    class Meta :
        model = Book
        fields = '__all__'