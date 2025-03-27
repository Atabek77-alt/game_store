from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from .models import Post, PostCommentary
from django.contrib.auth.mixins import LoginRequiredMixin

from ..news.models import GameNews
from ..product.models import Category, Game


# Create your views here.
class BlogView(ListView):
    model = Post
    template_name = 'pages/blog.html'
    context_object_name = 'posts'
    queryset = Post.objects.all().order_by('-created_at')
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = GameNews.objects.all().order_by('-created_at')[:3]
        context['products'] = Game.objects.all().order_by('-created_at')[:3]
        return context



def search_by_title(request):
    query = request.GET.get("title")
    if query:
        posts = Post.objects.filter(title__iexact=query)
    else:
        posts = Post.objects.all()

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "pages/blog.html", {"posts": page_obj, "query": query})

class DetailBlogView(DetailView):
    template_name = 'pages/blog_detail.html'
    model = Post
    context_object_name = 'post'
    queryset = Post.objects.all()




    def blog_view(request):
        posts = Post.objects.all()[:2]
        return render(request, 'blog.html', {'posts': posts})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.post_comments.all()
        context['posts'] = Post.objects.all().order_by('-created_at')[:3]

        return context


class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        user = request.user if request.user.is_authenticated else None
        comment_text = request.POST.get('comment_text')

        if comment_text:
            PostCommentary.objects.create(post=post, user=user, comment_text=comment_text)

        return redirect('blog_detail', pk=post_id)
