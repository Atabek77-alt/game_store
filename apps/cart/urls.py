from django.urls import path
from .views import CartGenericView
from . import views

# app_name = 'cart'

urlpatterns = [
    path('cart/<str:action>/<int:cart_item_id>/', CartGenericView.as_view(), name='cart_action'),
    path('cart/' , views.CartGenericView.as_view(), name='view_cart'),
]


