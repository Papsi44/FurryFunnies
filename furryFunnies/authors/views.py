from django.shortcuts import render, redirect

from furryFunnies.authors.forms import AuthorCreateForm, AuthorEditForm
from furryFunnies.authors.models import Author
from furryFunnies.utils import get_user_obj


def create_autor(request):
    form = AuthorCreateForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
               }

    return render(request, 'authors/create-author.html', context)


def edit_autor(request):
    author = get_user_obj()

    if request.method == 'POST':
        form = AuthorEditForm(request.POST or None, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author-details')
    else:
        form = AuthorEditForm(instance=author)
    context = {
        'form': form,
        'author': author,
    }
    return render(request, 'authors/edit-author.html', context)


def delete_autor(request):
    author = get_user_obj()
    if request.method == 'POST':
        author.delete()
        return redirect('index')
    return render(request, 'authors/delete-author.html')


def details_autor(request):
    author = get_user_obj()
    context = {
        'author': author,
    }
    return render(request, 'authors/details-author.html', context)
