from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('confirm/',views.confirm,name='confirm'),
    path('pre_confirm/',views.pre_confirm,name='pre_confirm'),
    path('cancel_order/',views.cancel_order,name='cancel_order'),
    path('pre_cancel',views.pre_cancel, name='pre_cancel')
]