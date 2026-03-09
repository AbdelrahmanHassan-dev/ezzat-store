from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class Signup(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = CustomUser
        fields = ('username','phone_number','phone_number_whatsapp','email','password1','password2',)

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','phone_number','phone_number_whatsapp','email']

        