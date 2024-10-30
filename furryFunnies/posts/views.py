from django.shortcuts import render, redirect

from furryFunnies.posts.forms import PostAddForm, PostDeleteForm, PostEditForm
from furryFunnies.posts.models import Post
from furryFunnies.utils import get_user_obj


def create_post(request):
    author = get_user_obj()
    form = PostAddForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(False)
            post.author = author
            post.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'posts/create-post.html', context)


def edit_post(request, post_id):
    author = get_user_obj()
    post = Post.objects.get(pk=post_id)

    if request.method == "POST":
        form = PostEditForm(request.POST or None, instance=post)
        if form.is_valid():
            post.save()
            return redirect('dashboard')
    else:
        form = PostEditForm(instance=post)

    context = {
        'form': form,
        'author': author,
        'post': post,
    }

    return render(request, 'posts/edit-post.html', context)


def delete_post(request, post_id):
    author = get_user_obj()
    post = Post.objects.get(pk=post_id)
    form = PostDeleteForm(request.POST or None, instance=post)
    if request.method == "POST":
        post.delete()
        return redirect('dashboard')
    context = {'form': form,
               'post': post,
               'author': author
               }
    return render(request, 'posts/delete-post.html', context)


def details_post(request, post_id):
    author = get_user_obj()
    post = Post.objects.get(pk=post_id)

    context = {
        'post': post,
        'author': author,
    }
    return render(request, f'posts/details-post.html', context)
