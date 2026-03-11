from django.urls import path
from . import views
# app_name = 'products'
urlpatterns = [
    path('',views.all_products,name='all_products'),
    path('product_details/<int:id>/',views.product_details,name="product_details"),
    path('saving_order_sessions/',views.saving_order_sessions,name='saving_order_sessions'),
    path('search/',views.search,name='search'),
    path('comments/',views.comment,name='comment'),
    
]