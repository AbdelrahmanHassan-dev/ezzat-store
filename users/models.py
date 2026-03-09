from django.db import models
from django.contrib.auth.models import AbstractUser 
from phonenumber_field.modelfields import PhoneNumberField #that is for the phone_number verfied 


class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(region="EG")
    phone_number_whatsapp = PhoneNumberField(region="EG",null=False, blank=False)




