from django.shortcuts import render,get_object_or_404,redirect
from .models import Product
from django.db.models import Q


def all_products(request):
    products = Product.objects.all()
    return render(request,'products/all_products.html',{'products':products})


def product_details(request,id):
    product = get_object_or_404(Product,id=id)
    return render(request,'products/product_details.html',{'product':product})



def saving_order_sessions (request):
    if request.method == "POST":
        product_id = request.POST.get('id')
        quantity = request.POST.get('quantity')

        request.session['product_id'] = product_id
        request.session['quantity'] = quantity
        return redirect('orders:confirm')
    return render(request,'products/product_details.html')



def search(request):
    if request.method == "GET":
        search_query = request.GET.get('product',None)
        if search_query == None:
            return render(request,'products/search.html',{'query':search_query, 'products':None})
        product = Product.objects.filter(Q(name_product__icontains=search_query)|Q(description__icontains=search_query)|Q(price__icontains=search_query)|Q(date_adding__icontains=search_query)).distinct()
        if product :
            return render(request,'products/search.html',{'query':search_query, 'products':product})
        return render(request,'products/search.html',{'query':search_query, 'products':None})
    
    else:
        return render(request,'products/search.html',{'query':search_query, 'products':None})