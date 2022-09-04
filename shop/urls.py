from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('', ShopHome.as_view(), name='index'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', ShopCategory.as_view(), name='category'),
    path('sellthing/', SellThing.as_view(), name='sell_thing'),
    path('useditems/', UsedItems.as_view(), name='useditems'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='shop/logout.html'), name='logout'),
    path('contact/', ContactFormView.as_view(), name="contact")
]
