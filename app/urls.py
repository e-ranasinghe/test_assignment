from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='hello'),
    path('post/new/', views.post_new, name='post_new'),
]