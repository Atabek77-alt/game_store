from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from .forms import ContactUsForm
from ..blog.models import Post
from ..news.models import GameNews
from ..product.models import Game, Category


class HomeView(TemplateView):
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-created_at')[:2]
        context['products'] = Game.objects.all().order_by('-created_at')[:4]
        context['news'] = GameNews.objects.all().order_by('-created_at')[:6]
        context['categories'] = Category.objects.all()
        return context

def search_by_title(request):
    query = request.GET.get("search", "")
    results = Game.objects.filter(title__icontains=query) if query else []
    return render(request, "pages/base.html", {"results": results, "query": query})



class ContactUs(CreateView):
    template_name = 'pages/contact_us.html'
    form_class = ContactUsForm
    success_url = '/'


