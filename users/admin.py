from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.html import format_html
from orders.models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','product','quantity','total_price','status','user_phone','his_whatsapp','created_at']
    list_editable = ['status', 'quantity']
    list_filter = ['status','created_at']
    search_fields = ['user__username','product__name_product']

    readonly_fields = ['total_price', 'created_at', 'user_phone','his_whatsapp']
    def user_phone(self,obj):
        return obj.user.phone_number_whatsapp

    def his_whatsapp(self,obj):
        phone = obj.user.phone_number_whatsapp
        if phone :
            url = f"https://wa.me/{phone}?text=hello!%20we%20are%20Hot%20price"
            return format_html('<a href="{}" target="_blank" style="color: #25D366; font-weight: bold;">WhatsApp User</a>', url)
        phone_number= obj.user.phone_number
        return f"he didn't put whatsapp number call him{phone_number}"


admin.site.register(Order, OrderAdmin)







# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser

# @admin.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     list_display = UserAdmin.list_display + ('phone_number', 'phone_number_whatsapp')

#     fieldsets = list(UserAdmin.fieldsets)
#     fieldsets[1][1]['fields'] += ('phone_number', 'phone_number_whatsapp')   


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + (
        'whatsapp_link',
        'phone_number',
        'phone_number_whatsapp',
    )

    fieldsets = list(UserAdmin.fieldsets)
    fieldsets[1][1]['fields'] += ('phone_number', 'phone_number_whatsapp')

    def whatsapp_link(self, obj):
        if obj.phone_number_whatsapp:
            url = f"https://wa.me/{obj.phone_number_whatsapp}?text=New order"
            return format_html('<a href="{}" target="_blank">Open WhatsApp</a>', url)
        return "-"

    whatsapp_link.short_description = "WhatsApp"