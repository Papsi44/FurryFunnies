from django.shortcuts import render


def create_post(request):
    return render(request, 'posts/create-post.html')


def edit_post(request):
    return render(request, 'posts/edit-post.html')


def delete_post(request):
    return render(request, 'posts/delete-post.html')


def details_post(request):
    return render(request, 'posts/details-post.html')