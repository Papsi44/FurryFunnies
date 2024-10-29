from django.shortcuts import render, redirect

from furryFunnies.posts.forms import PostAddForm
from furryFunnies.utils import get_user_obj


def create_post(request):
    form = PostAddForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'posts/create-post.html', context)


def edit_post(request):
    return render(request, 'posts/edit-post.html')


def delete_post(request):
    return render(request, 'posts/delete-post.html')


def details_post(request):
    return render(request, 'posts/details-post.html')