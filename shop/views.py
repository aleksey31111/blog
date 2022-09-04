from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from .models import Shop, Category, SellThing
from .forms import *
from .utils import *


class ShopHome(DataMixin, ListView):
    model = Shop
    template_name = "shop/index.html"
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Страница магазина'
        # context['cat_selected'] = 0
        # context['menu'] = menu
        # return context
        c_def = self.get_user_context(title="Страница магазина")
        return dict(list(context.items()) + list(c_def.items()))

    def shop_list(request, category_slug=None):
        category = None
        categories = Category.objects.all()
        products = Shop.objects.filter(available=True)
        if category_slug:
            category = get_object_or_404(Category, sllug=category_slug)
            products = products.filter(category=category)

    def get_queryset(self):
        return Shop.objects.filter(is_available=True).select_related('cat')


class ShowPost(DataMixin, DetailView):
    model = Shop
    template_name = 'shop/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = context['post']
        # context['menu'] = menu
        # return context
        c_def = self.get_user_context(title=context["post"])
        return dict(list(context.items()) + list(c_def.items()))


class ShopCategory(DataMixin, ListView):
    model = Shop
    template_name = "shop/index.html"
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Shop.objects.filter(cat__slug=self.kwargs['cat_slug'],
                                   is_available=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        # context['cat_selected'] = context['posts'][0].cat_id
        # context['menu'] = menu
        # return context
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - ' +
                                            str(c.name),
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))


class UsedItems(ListView):
    model = SellThing

    template_name = 'shop/useditems.html'
    context_object_name = 'useditems'

    # def index(request):
    #     return {
    #     'name': SellThing.name,
    #     'thing': SellThing.thing,
    #     'foto': SellThing.foto,
    #     'description': SellThing.description,
    #     'passport': SellThing.passport,
    #     'time': SellThing.time,
    #     'time_safe': SellThing.time_safe,
    #     'place': SellThing.place,
    #     'defect_uot': SellThing.defect_out,
    #     'defect_in': SellThing.defect_in,
    #     'is_available': SellThing.is_available,
    # }

    # def get_queryset(self):
    #     return UsedItems.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Продажа устройств'
        # context['cat_selected'] = 0
        context['menu'] = menu

        return context
        # c_def = self.get_user_context(title="Подержанные устройства")
        # return dict(list(context.items()) + list(c_def.items()))


class SellThing(DataMixin, CreateView):
    model = SellThing
    fields = '__all__'
    template_name = 'shop/sellthing.html'
    context_object_name = "sellthing"

    # success_url = reverse_lazy("index")
    # login_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Продать вещь")
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'shop/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'shop/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'shop/contact.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Обратная связь')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('index')
