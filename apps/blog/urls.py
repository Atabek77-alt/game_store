from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogView.as_view(), name = 'blog'),
    path('post/<int:pk>/', DetailBlogView.as_view(), name='blog_detail'),
    path('blog/<int:post_id>/add_comment/', AddCommentView.as_view(), name='add_comment'),
    path("blog/search/", search_by_title, name="search_by_title"),
]





