from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'hello.html')


@login_required(login_url='/accounts/login/')
def post_new(request):
    form = PostForm()
    return render(request, 'post.html', {'form': form})
