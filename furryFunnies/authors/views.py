from django.shortcuts import render, redirect

from furryFunnies.authors.forms import AuthorCreateForm
from furryFunnies.utils import get_user_obj


def create_autor(request):
    form = AuthorCreateForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    #     else:
    #         print(form.errors)
    #         # Form is not valid, errors will be in `form.errors`
    #         return render(request, 'authors/create-author.html', {'form': form})
    # else:
    #     form = AuthorCreateForm()

    context = {
        'form': form,
               }

    return render(request, 'authors/create-author.html', context)


def edit_autor(request):
    return render(request, 'authors/edit-author.html')


def delete_autor(request):
    return render(request, 'authors/delete-author.html')


def details_autor(request):
    return render(request, 'authors/details-author.html')
