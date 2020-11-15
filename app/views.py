from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from django.contrib.auth.decorators import login_required


@login_required
def hello(request):
    return render(request, 'app/hello.html')


@login_required
def post_new(request):
    form = PostForm()
    return render(request, 'post.html', {'form': form})
