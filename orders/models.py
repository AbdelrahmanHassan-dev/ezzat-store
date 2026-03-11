from django.db import models
from django.utils import timezone
from users.models import CustomUser
from products.models import Product, Comment
from django_countries.fields import CountryField

class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED','Approved'),
        ('REJECTED','rejected'),
        ('CANCELLED','cancelled'),
        ('COMPLETED', 'Completed'),
    ]
    EGYPT_GOVERNORATES = [
        ('cairo', 'Cairo'),
        ('alexandria', 'Alexandria'),
        ('giza', 'Giza'),
        ('port_said', 'Port Said'),
        ('suez', 'Suez'),
        ('luxor', 'Luxor'),
        ('asyut', 'Asyut'),
        ('ismailia', 'Ismailia'),
        ('minya', 'Minya'),
        ('qena', 'Qena'),
        ('faiyum', 'Fayoum'),
        ('zagazig', 'Zagazig'),
        ('tanta', 'Tanta'),
        ('damanhur', 'Damanhur'),
        ('el_mahalla_el_kubra', 'El Mahalla El Kubra'),
        ('banha', 'Banha'),
        ('aswan', 'Aswan'),
        ('mit_gammur', 'Mit Gammur'),
        ('shibin_el_kom', 'Shibin El Kom'),
        ('bani_suef', 'Beni Suef'),
        ('arish', 'Arish'),
        ('kafr_el_sheikh', 'Kafr El Sheikh'),
        ('matruh', 'Matrouh'),
        ('dakahlia', 'Dakahlia'),
        ('sharqia', 'Sharqia'),
        ('gharbia', 'Gharbia'),
        ('monufia', 'Monufia'),
        ('qalyubia', 'Qalyubia'),
        ('new_valley', 'New Valley'),
        ('north_sina', 'North Sinai'),
        ('south_sina', 'South Sinai'),
        ('red_sea', 'Red Sea'),
    ]
    pickup_location = models.CharField(max_length=300)
    city_choices = models.CharField(
        max_length=100,
        choices=EGYPT_GOVERNORATES,
        blank=True,
        null=True
    )

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
        
