from django.db.models import Count
from .models import *

menu = [
    {'title': 'Продать вещь', 'url_name': 'sell_thing'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    # {'title': 'Регистрация', 'url_name': 'register'},
    # {'title': 'Войти', 'url_name': 'login'},
]


class DataMixin:
    paginate_by = 4
    def get_user_context(self, **kwargs):
        context = kwargs
        cat = Category.objects.annotate(Count('shop'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(0)

        context['menu'] = user_menu
        context['cats'] = cat

        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context


