from django.shortcuts import render,redirect
from .forms import Signup, UpdateUserForm
from django.contrib.auth.decorators import login_required
from orders.models import Order
def signup(request):
    if request.method =="POST":
        form = Signup(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = Signup()
    return render(request,'home/signup.html',{'form':form})



@login_required
def profile(request):
    orders = Order.objects.filter(user=request.user)

    return render(request,'users/profile.html',{'user':request.user,'orders':orders})

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

@login_required
def edit_profile(request):
    if request.method=="POST":
        if 'update_info' in request.POST:
            user_form = UpdateUserForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user_form.save()

        elif 'change_password' in request.POST:
            password_form = PasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request,user)

    user_form = UpdateUserForm(instance=request.user)
    password_form = PasswordChangeForm(request.user)



    orders = Order.objects.filter(user=request.user)

    return render(request, 'users/edit_profile.html', {
        'user_form': user_form,
        'password_form': password_form,
        'orders': orders
    })