from django.contrib import admin
from .models import Product, Product_images,Comment
from orders.models import Order

class Produt_imagesInline(admin.TabularInline):
    model = Product_images
    extra = 2

class ProductAdmin(admin.ModelAdmin):
    inlines = [Produt_imagesInline]



admin.site.register(Product,ProductAdmin)
admin.site.register(Product_images)
admin.site.register(Comment)


