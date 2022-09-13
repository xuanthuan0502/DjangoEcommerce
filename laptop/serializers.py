from curses import meta
from .models import Laptop
from rest_framework import serializers

#class LaptopSerializer(serializers.Serializer):
 #   name = serializers.CharField(max_length=200)
  #  code = serializers.CharField(max_length=200)
    

class LaptopSerializer(serializers.ModelSerializer):
    #name = serializers.CharField(max_length=200)
    #code = serializers.CharField(max_length=200)
    class Meta :
        model = Laptop
        fields = '__all__'
