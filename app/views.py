from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.utils import timezone

from .forms import PostForm
from .models import Post


@login_required
def hello(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')[:3]
    return render(request, 'app/hello.html', {'posts': posts})


@login_required
def next_posts(request):
    page = request.POST.get('page')
    posts = Post.objects.filter(published=True).order_by('-created_at')

    results_per_page = 3
    paginator = Paginator(posts, results_per_page)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(2)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    posts_html = loader.render_to_string('app/posts.html', {'posts': posts})

    output_data = {'posts_html': posts_html, 'has_next': posts.has_next()}
    return JsonResponse(output_data)


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
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'app/post_new.html', {'form': form})


@login_required
def post_detail(request, pk):
    posts = Post.objects.filter(published=True).order_by('-created_at')[:3]
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'app/post_view.html', {'curr_post': post, 'posts': posts})
