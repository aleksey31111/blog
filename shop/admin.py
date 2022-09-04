from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import *


class ShopAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Shop
        fields = '__all__'


class ShopAdmin(admin.ModelAdmin):
    form = ShopAdminForm
    prepopulated_fields = {"slug": ("thing",)}
    list_display = ('id', 'cat', 'thing', 'description', 'foto', 'cost',
                    'time', 'time_update', 'is_available')
    list_display_links = ('cat', 'thing', 'foto')
    search_fields = ('thing', 'cost', 'time', 'description')
    list_editable = ('is_available',)
    list_filter = ('is_available', 'time')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("name",)}
    list_display = ('id', 'name', 'slug')
    list_display_links = ('name',)
    search_fields = ('name',)


class SellThingAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)
    passport = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = SellThing
        fields = '__all__'


class SellThingAdmin(admin.ModelAdmin):
    form = SellThingAdminForm
    # prepopulated_fields = {'name': ('thing',)}
    list_display = ('id', 'thing', 'passport', 'time', 'time_safe', 'place', 'defect_out', 'defect_in','is_available')
    list_display_links = ('thing',)
    search_fields = ('id', 'name', 'thing', 'passport')
    list_editable = ('is_available',)



admin.site.register(Shop, ShopAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SellThing, SellThingAdmin)
