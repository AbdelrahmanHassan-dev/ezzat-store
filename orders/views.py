from django.shortcuts import render,redirect,get_object_or_404
from .models import Order
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.db import transaction


from django.db.models import F


@login_required
@transaction.atomic 
def confirm(request):

    product_id = request.session.get('product_id')
    quantity = request.session.get('quantity',1)
    pickup_location = request.session.get('pickup_location')
    city_choices = request.session.get('city_choices')
    if not product_id:
        return redirect('all_products')
    product = get_object_or_404(Product,id=product_id)
    if int(quantity) > int(product.stock):
        messages.error(request,"Requested quantity exceeds stock.")
        return redirect('product_details',id=product_id)
    order = Order.objects.create(
        user = request.user,
        product= product,
        quantity = quantity,
        pickup_location=pickup_location,
        city_choices=city_choices
    )



    product.stock = F('stock') - quantity
    product.save()

    if product.stock<=0:
        product.is_available= False
        product.save()
    del request.session['product_id']
    del request.session['quantity']
    return render(request,'products/confirm.html',{'order':order})


def pre_confirm(request):
    product_id = None
    quantity = None
    pickup_location = None
    city_choices=None
    if request.method == "POST":
        product_id = request.POST.get('id')
        quantity = request.POST.get('quantity')
        pickup_location = request.POST.get('pickup_location')
        city_choices = request.POST.get('city_choices')
    if not product_id:
        product_id = request.session.get('product_id')
    if not quantity:
        quantity = request.session.get('quantity',1)
    if not pickup_location:
        pickup_location = request.session.get('pickup_location')
    if not city_choices:
        city_choices= request.session.get('city_choices')
    product =get_object_or_404(Product,id=product_id)
    
    amount = float(quantity)*float(product.price)
    # city_choices= Order.EGYPT_GOVERNORATES
    try :
        quantity = int(quantity)
        if quantity < 1:
            messages.error(request,"you can't put negative number")
            return render(request, 'products/product_details.html',{'product':product})
    
        if quantity > product.stock:
            messages.error(request,"unfortunately, we don't have this quantity in our stock")
            return render(request, 'products/product_details.html',{'product':product})

    except ValueError:
        messages.error(request,"the quantity have to be INT")
        return render(request,'products/product_details.html',{'product':product})
    return render(request,'products/pre_confirm.html',{'amount':amount,'quantity':quantity,'product':product,'pickup_location':pickup_location,'city_choices':city_choices})

@login_required
def cancel_order(request):
    if request.method == "POST":
        order_id = request.POST.get('order_id')
        order = get_object_or_404(Order,id=order_id,user=request.user)
        # order.delete() #instead deleting I think it will be better if we save it in the database maybe we will need it, to know like there are someone want it 
        quantity = order.quantity
        selected_product = order.product.id
        source_product = get_object_or_404(Product,id=selected_product)
        if order.status != 'CANCELLED':
            source_product.stock += int(quantity)
            source_product.save()
        order.status= 'CANCELLED'
        order.save()

        if source_product.stock >= 0:
            source_product.is_available= True
            source_product.save()

        messages.error(request,"You delete the item.")
        return redirect('profile')
    return render(request,'products/cancel_order.html')


@login_required
def pre_cancel(request):
    if request.method == "POST":
        order_id = request.POST.get('order_id')
        order = get_object_or_404(Order,id=order_id, user= request.user)        
    return render(request,'products/cancel_order.html',{'order':order})
    
