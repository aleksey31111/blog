from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # whats_happen = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    service_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # foto = forms.ImageField(upload_to='repairDevice/')
    # not_work = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))