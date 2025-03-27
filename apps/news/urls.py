
from django.urls import path
from .views import *

urlpatterns = [
    path('', NewsView.as_view(), name = 'news'),
    path('news/<int:pk>/', DetailNewsView.as_view(), name='news_detail'),
    path('news/<int:post_id>/add_comment/', AddCommentView.as_view(), name='comment')
]