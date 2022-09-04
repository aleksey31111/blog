from django.shortcuts import render

from .models import CmsSlider
from price.models import PriceTable, PriceCard
from crm.models import Order
from crm.forms import OrderForm
from telebot.sendmessage import send_telegram


def first_page(request):
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    form = OrderForm()
    price_table = PriceTable.objects.all()
    dict_obj = {
        'slider_list': slider_list,
        'pc_1': pc_1,
        'pc_2': pc_2,
        'pc_3': pc_3,
        'price_table': price_table,
        'form': form,
    }
    return render(request, 'cms/index.html', dict_obj)


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        service_name = request.POST['service_name']
        element = Order(order_name=name, order_phone=phone, order_service_name=service_name)
        element.save()
        send_telegram(tg_name=name, tg_phone=phone, tg_service_name=service_name)
        return render(request, 'cms/thanks.html', {'name': name})
    else:
        return render(request, 'cms/thanks.html')
