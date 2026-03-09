from django.db import models
from django.utils import timezone
from users.models import CustomUser
from products.models import Product, Comment
class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED','Approved'),
        ('REJECTED','rejected'),
        ('CANCELLED','cancelled'),
        ('COMPLETED', 'Completed'),
    ]

    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default = 'PENDING')
    quantity = models.IntegerField(default=1)
    
    @property
    def total_price(self):
        return int(self.product.price) * int(self.quantity)
    
    def __str__(self):
        return f"{self.user.username} ----> {self.product} / {self.total_price}"
        
