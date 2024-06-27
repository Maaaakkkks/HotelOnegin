from dataclasses import fields
from pyexpat import model
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import Users
from booking.models import Booking

class UserLoginForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={"autofocus": True, 'class': 'formm_controll' , 'placeholder': 'Ваша username..'}))
    password = forms.CharField(
        widget=forms.TextInput(attrs={"autocomplete": "current-password", 'class': 'formm_controll' , 'placeholder': 'Ваш пароль..'}))
    class Meta:
       model = Users
       fields = ['username', 'password'] 


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = Users
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )
    
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()
    password1 = forms.CharField()
    password2 = forms.CharField()


class ProfileForm(UserChangeForm):
    class Meta:
        model = Users
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",)

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField()


# class Booking(model.Booking):
#     class Meta:
#         model = Booking
#         fields = (
#             "first_name",
#             "last_name",
#             "username",
#             "email",)

#     first_name = forms.CharField()
#     last_name = forms.CharField()
#     username = forms.CharField()
#     email = forms.CharField()
    