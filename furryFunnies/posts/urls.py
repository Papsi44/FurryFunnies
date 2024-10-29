from django.urls import include, path

from furryFunnies.posts import views

urlpatterns = [
    path('create/', views.create_post, name='post-create'),
    path('<int:post_id>/', include([
        path('delete/', views.delete_post, name='post-delete'),
        path('details/', views.details_post, name='post-details'),
        path('edit/', views.edit_post, name='post-edit'),

        ])
    )

]