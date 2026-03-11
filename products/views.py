from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,Comment
from django.db.models import Q
from orders.models import Order
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def all_products(request):
    products = Product.objects.all()
    return render(request,'products/all_products.html',{'products':products})


def product_details(request,id):
    product = get_object_or_404(Product,id=id)
    city_choices= Order.EGYPT_GOVERNORATES

    return render(request,'products/product_details.html',{'product':product,'city_choices':city_choices})



def saving_order_sessions (request):
    if request.method == "POST":
        product_id = request.POST.get('id')
        quantity = request.POST.get('quantity')
        pickup_location =request.POST.get('pickup_location')
        city_choices = request.POST.get('city_choices')
        request.session['product_id'] = product_id
        request.session['quantity'] = quantity
        request.session['pickup_location'] = pickup_location
        request.session['city_choices'] = city_choices
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


@login_required
def comment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        product_id = request.POST.get('id')
        if comment:
            Comment.objects.create(
                user= request.user,
                text=comment,
                # product = (Product.objects.get(id = product_id)),
                product = (get_object_or_404(Product, id = product_id)),
            )
        messages.success(request, "Your comment was added successfully")

        return redirect('product_details',id=product_id)
    return redirect('all_products')


# @login_required
# def comment(request):
#     if request.method == "POST":
#         text = request.POST.get('comment')
#         product_id = request.POST.get('id')
        
#         if text:  # التأكد أن التعليق ليس فارغاً
#             product = get_object_or_404(Product, id=product_id)
#             Comment.objects.create(
#                 user=request.user,
#                 text=text,
#                 product=product
#             )
#             messages.success(request, "تم إضافة تعليقك بنجاح.")
        
#         # العودة لنفس صفحة المنتج بعد إضافة التعليق
#         return redirect('product_details', id=product_id)
    
#     return redirect('all_products')

