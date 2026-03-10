from django.urls import path
from . import views 
from products.views import all_products

urlpatterns = [
    path('home/',views.home,name='home'),
    path('',all_products , name = 'all_products')
]