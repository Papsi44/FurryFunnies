from django.urls import path

from furryFunnies.authors import views

urlpatterns = [
    path('create/', views.create_autor, name='author-create'),
    path('delete/', views.delete_autor, name='author-delete'),
    path('details/', views.details_autor, name='author-details'),
    path('edit/', views.edit_autor, name='author-edit'),

]