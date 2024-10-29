from django.shortcuts import render, redirect

from furryFunnies.posts.models import Post
from furryFunnies.utils import get_user_obj


def index(request):
    author = get_user_obj()
    if author:
        return redirect('dashboard')

    return render(request, 'common/index.html')


def dashboard(request):
    author = get_user_obj()
    if request.method == "GET":
        if not author:
            return redirect('index')
    posts = Post.objects.filter(author=author)
    context = {
        'author': author,
        'posts': posts
    }
    return render(request, 'common/dashboard.html', context)

