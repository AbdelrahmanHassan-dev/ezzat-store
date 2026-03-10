from django.db import models
from users.models import CustomUser
from django.utils import timezone



class Product(models.Model):
    name_product = models.CharField(max_length=50)
    description = models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=3)
    date_adding= models.DateField(auto_now_add=True)
    is_available = models.BooleanField()
    stock = models.PositiveIntegerField()



    def __str__(self):
        return self.name_product

class Product_images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='image')
    image= models.ImageField(upload_to="images/%Y/%m/%d/")


class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')