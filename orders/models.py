from django.db import models
from django.utils import timezone
from users.models import CustomUser
from products.models import Product, Comment
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _

class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING',   _('Pending')),
        ('APPROVED',  _('Approved')),
        ('REJECTED',  _('Rejected')),
        ('CANCELLED', _('Cancelled')),
        ('COMPLETED', _('Completed')),
    ]
    EGYPT_GOVERNORATES = [
        ('cairo',               _('Cairo')),
        ('alexandria',          _('Alexandria')),
        ('giza',                _('Giza')),
        ('port_said',           _('Port Said')),
        ('suez',                _('Suez')),
        ('luxor',               _('Luxor')),
        ('asyut',               _('Asyut')),
        ('ismailia',            _('Ismailia')),
        ('minya',               _('Minya')),
        ('qena',                _('Qena')),
        ('faiyum',              _('Fayoum')),
        ('zagazig',             _('Zagazig')),
        ('tanta',               _('Tanta')),
        ('damanhur',            _('Damanhur')),
        ('el_mahalla_el_kubra', _('El Mahalla El Kubra')),
        ('banha',               _('Banha')),
        ('aswan',               _('Aswan')),
        ('mit_gammur',          _('Mit Gammur')),
        ('shibin_el_kom',       _('Shibin El Kom')),
        ('bani_suef',           _('Beni Suef')),
        ('arish',               _('Arish')),
        ('kafr_el_sheikh',      _('Kafr El Sheikh')),
        ('matruh',              _('Matrouh')),
        ('dakahlia',            _('Dakahlia')),
        ('sharqia',             _('Sharqia')),
        ('gharbia',             _('Gharbia')),
        ('monufia',             _('Monufia')),
        ('qalyubia',            _('Qalyubia')),
        ('new_valley',          _('New Valley')),
        ('north_sina',          _('North Sinai')),
        ('south_sina',          _('South Sinai')),
        ('red_sea',             _('Red Sea')),
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
        
