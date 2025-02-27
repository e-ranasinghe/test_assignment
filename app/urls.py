from django.urls import path

from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('next_posts/', views.next_posts, name='next_posts'),
]