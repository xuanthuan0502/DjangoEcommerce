from django.shortcuts import render
from rest_framework import status
from django.http import HttpResponse
from .models import Laptop
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import LaptopSerializer
from rest_framework.views import APIView
import json

# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    laptop_list = Laptop.objects.order_by('name')
    return render(request,"home.html",{'laptop_list' : laptop_list})

#def rest(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
 #   laptop_list = Laptop.objects.order_by('name')
  #  laptop_name = [{"name":Laptop.name} for Laptop in laptop_list]
   # return HttpResponse(json.dumps(laptop_name), content_type='application/json')

#def rest(request,laptop_id=None):
 #   laptop_list = Laptop.objects.all()
  #  if laptop_id:
   #     laptop_list = laptop_list.filter(id=laptop_id)
   # if 'type' in request.GET and request.GET['type'] == 'xml':
   #     serialized_laptops = serializers.serialize('xml',laptop_list)
   #     return HttpResponse(serialized_laptops, content_type='application/xml')
   # else:
    #    serialized_laptops = serializers.serialize('json',laptop_list)
    #return HttpResponse(serialized_laptops, content_type='application/json')




@api_view(['GET','POST','DELETE'])
def rest_Laptop(request):
    if request.method == 'GET':
        laptops = Laptop.objects.all()
        serializer = LaptopSerializer(laptops, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        
        mydata = LaptopSerializer(data = request.data)
        if not mydata.is_valid():
            return Response('Sai du lieu roi')
        mydata.save()
        return Response('them thanh cong')
        ... #logic for HTTP POST operation
    
@api_view(['GET', 'PUT', 'DELETE'])
def laptop_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        laptop = Laptop.objects.get(pk=pk)
    except Laptop.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LaptopSerializer(laptop)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LaptopSerializer(laptop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        laptop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

