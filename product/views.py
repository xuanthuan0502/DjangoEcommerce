from datetime import datetime
from django.shortcuts import redirect, render, HttpResponseRedirect
from .models import Payment, Product,CartItem,Shipment,Order,OrderItem
from laptop.models import Laptop
from book.models import Book
from mobilePhone.models import MobilePhone
from customer.models import Customer
from django.contrib.auth.hashers import  check_password
import json
from json import JSONEncoder
from django.core import serializers
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
# Create your views here.
class ProductEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    product_list = Product.objects.order_by('name')
    return render(request,"index.html",{'product_list' : product_list})

def single_product(request,pk):
    #return HttpResponse("Hello, world. You're at the polls index.")

    product_detail = Product.objects.get(pk=pk)
    product = product_detail
    if product_detail.category == 'laptop':
        product_detail = Laptop.objects.get(pk=pk)
    elif product_detail.category == 'book':
        product_detail = Book.objects.get(pk=pk)  
    elif  product_detail.category == 'mobilephone': 
        product_detail = MobilePhone.objects.get(pk=pk)  
    product_detail = json.dumps(product_detail,indent=4, cls=ProductEncoder)
    customerid = request.session.get('customerid')
    customer = Customer.objects.filter(id = customerid)
    if request.method == 'POST' and customer:
        customer = Customer.objects.get(id = customerid)
        quantity = request.POST.get ('quantity')
        cartitem = CartItem(product= product,customer = customer, quantity=quantity, price=product.price)
        cartitem.register()
        return redirect('/product/index')
        
    return render(request,"single-product.html",{'product_detail' : product_detail,'product' : product})    

def cart(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    customerid = request.session.get('customerid')
    customer = Customer.objects.filter(id = customerid)
    if request.method == 'POST':
        cartitem_list = CartItem.objects.all().filter(customer = customerid)
        total = 0
        order_list = []
        for item in cartitem_list:
            a = str(item.id)
            value = request.POST.get (''+a)
          #  order_list =         
            if value :
                print(value)
                price = item.get_total()
                total = total+price
                order_list.append(item.id)
        if total > 0 :
            request.session['order_list'] = order_list
            request.session['total_price'] = total
            return HttpResponseRedirect('checkout')
            
    if customer:
        cartitem_list = CartItem.objects.all().filter(customer = customerid)
        total = 0
        
        for item in cartitem_list:
            price = item.get_total()
            total = total+price
        return render(request,"cart.html",{'cartitem_list' : cartitem_list, 'total_price' : total})
   
def checkout(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    order_list = request.session.get('order_list')
    total =  request.session.get('total_price')
    customerid = request.session.get('customerid')
   
    list = []
    for id in order_list :
        item = CartItem.objects.get(id = id)
        list.append(item)
    order_list = list
    customer = Customer.objects.get(id =customerid )
    if request.method == 'POST' and customer:
        name =  request.POST.get('name')
        email =  request.POST.get('email')
        phone =  request.POST.get('phone')
        address =  request.POST.get('address')
        payment_name = request.POST.get('payment_method')      
        payment = Payment.objects.get(name = payment_name)
        order = Order(customer = customer,payment = payment,price = total)
        order.register()

        shipment = Shipment(order = order, name = name,  phone = phone,email = email, address = address)
        shipment.register()
        for item in order_list:
            
            orderitem = OrderItem(product=item.product,order=order,quantity=item.quantity,price = item.price)
            orderitem.register()
            item.delete()
        del request.session['order_list']
        del request.session['total_price']
        return redirect('/product/cart')


    return render(request,"checkout.html",{'order_list' : order_list, 'total_price' : total }) 

def order(request):
    order_list = Order.objects.all()
    return render(request,"order.html",{'order_list' : order_list }) 

def orderlist(request,pk):
    total = 0
    order = Order.objects.get(id = pk)
    list_orderitem = OrderItem.objects.all().filter(order = pk)
    for item in list_orderitem:
        total = total+item.price
    return render(request,"orderlist.html",{'list_orderitem' : list_orderitem, 'total_price' : total,'time' : order.date_added})

def login(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
  
    if request.method == 'POST':
        loginname = request.POST.get ('name')
        password = request.POST.get ('pass')
        print (loginname, password)
        customer = Customer.objects.get(loginname = loginname)
        
        if customer and password == customer.password  :
            request.session['customerid'] = customer.id
            request.session['customername'] = customer.name
            return HttpResponseRedirect('index')
   # request.session['']
    return render(request,"login.html") 

def logout(request):
    request.session.clear()
    return HttpResponseRedirect('index')

def signup(request):
    if request.method == 'POST':
        loginname = request.POST.get ('loginname')
        name = request.POST.get ('name')
        password = request.POST.get ('pass')
        repassword = request.POST.get ('repass')
        email = request.POST.get ('email')
        phone = request.POST.get ('phone')
        customer = Customer.objects.filter(loginname = loginname)
        if not customer and password == repassword :
            customer = Customer (name=name,
                                loginname=loginname,
                              password= password,
                             email=email,
                             phone=phone,
                             )
            customer.register()
            return HttpResponseRedirect('login')
    return render(request,"signup.html")
@csrf_protect
def delete(request,pk) :
    CartItem.objects.filter(id =pk).delete()
    #csrfContext = RequestContext(request)
    return render(request,'cart.html')

