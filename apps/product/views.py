from django.shortcuts import render ,get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, View
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from ..blog.models import Post




class CatalogView(ListView):
    model = Game
    template_name = 'pages/catalog.html'
    context_object_name = 'products'
    paginate_by = 7
    queryset = Game.objects.all().order_by('title')

    def get_queryset(self):
        query = self.request.GET.get('title', '')
        if query:
            return Game.objects.filter(title__icontains=query).order_by('title')
        return Game.objects.all().order_by('title')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('title', '')
        return context



class ProductView(ListView):
    model = Game
    template_name = 'pages/store.html'
    context_object_name = 'products'
    queryset = Game.objects.all().order_by()
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-created_at')[:3]
        return context











class DetailProView(DetailView):
    template_name = 'pages/product_detail.html'
    model = Game
    context_object_name = 'product'
    queryset = Game.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['posts'] = Post.objects.all().order_by('-created_at')[:3]
        context['categories'] = Category.objects.all()
        context['products'] = Game.objects.all().order_by('-created_at')[:4]
        return context

    def game_detail(request, id):
        products = get_object_or_404(Game, id=id)
        return render(request, 'product_detail.html', {'products': products })

class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, post_id):

        game = get_object_or_404(Game, id=post_id)

        comment_text = request.POST.get('comment_text')


        Comment.objects.create(game=game, user=request.user, text=comment_text)

        return redirect('product_detail', pk=post_id)













