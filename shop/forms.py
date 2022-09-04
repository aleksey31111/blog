from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField
from django.contrib.auth.models import User
from .models import *
from captcha.fields import CaptchaField

# class SellThingForm(forms.ModelForm):
#     captcha = CaptchaField()
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         self.fields['cat'].empty_label = "Нужно выбрать 'Подержанные продаются в магазин'"
#
#     class Meta:
#         model = Shop
#         fields = ['thing', 'slug', 'description', 'foto',
#                   'cost', 'is_available', 'cat']
#         widgets = {
#             'thing': forms.TextInput(attrs={'class': 'form-input'}),
#             'slug': forms.TextInput(attrs={'class': 'form-input'}),
#             'description': forms.Textarea(attrs={'cols': 40, 'rows': 13,
#                                                  'class': 'form_input'}),
#
#             'cost': forms.TextInput(attrs={'class': 'form-input'}),
#             'is_available': forms.Textarea(attrs={'cols': 6, 'rows': 1, 'class': 'form-input'}),
#         }
#
#     def clean_thing(self):
#         thing = self.cleaned_data['thing']
#         if len(thing) >300:
#             raise ValidationError("Длинна превышает 300 символов")
#         return thing


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ContactForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField(label="Email")
    content = forms.CharField(label="Сообщение", widget=forms.Textarea(attrs={'cols': 70, 'rows': 13}))
    captcha = CaptchaField()
