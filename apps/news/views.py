from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from .models import *
from .models import Game
from ..blog.models import Post

from django.core.paginator import Paginator

from ..product.models import Comment


class NewsView(ListView):
    model = GameNews
    template_name = 'pages/news.html'
    context_object_name = 'news'
    queryset = GameNews.objects.all().order_by('-created_at')
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        context['categories'] = Category.objects.all()
        context['posts'] = Post.objects.all().order_by('-created_at')[:3]

        category_name = self.request.GET.get('category')
        if category_name:
            category = Category.objects.get(name=category_name)
            context['news'] = GameNews.objects.filter(category=category).order_by('-created_at')
        else:
            context['news'] = GameNews.objects.all().order_by('-created_at')

        paginator = Paginator(context['news'], self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['news'] = page_obj
        return context


class DetailNewsView(DetailView):
    template_name = 'pages/news_detail.html'
    model = GameNews
    context_object_name = 'new'
    queryset = GameNews.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-created_at')[:3]
        return context


class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, post_id):

        news = get_object_or_404(GameNews, id=post_id)

        comment_text = request.POST.get('comment_text')

        Comment.objects.create(comment=news, user=request.user, text=comment_text)

        return redirect('news_detail', pk=post_id)
