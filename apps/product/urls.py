
from django.urls import path
from .views import *

urlpatterns = [
    path('store/', ProductView.as_view(), name = 'product1'),
    path('product/<int:pk>/', DetailProView.as_view(), name='product_detail'),
    path('catalog/', CatalogView.as_view(), name = 'product'),
    path('product/<int:post_id>/add_comment/', AddCommentView.as_view(), name='add_comment'),
]