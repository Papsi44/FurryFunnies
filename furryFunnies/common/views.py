from django.shortcuts import render, redirect

from furryFunnies.utils import get_user_obj


def index(request):
    author = get_user_obj()
    if author:
        return redirect('dashboard')

    return render(request, 'common/index.html')


def dashboard(request):
    author = get_user_obj()
    if not author:
        return redirect('index')
    context = {
        'author': author
    }
    return render(request, 'common/dashboard.html', context)

