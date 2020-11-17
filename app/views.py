from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils import timezone


@login_required
def hello(request):
    return render(request, 'app/hello.html')


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.created_at = timezone.now()
            post.published = True
            post.save()
            return redirect('hello')
    else:
        form = PostForm()
    return render(request, 'app/post_new.html', {'form': form})
