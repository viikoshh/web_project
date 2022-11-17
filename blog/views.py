from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.http import Http404

from .models import Post
from .forms import PostForm


def post_add(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', id=post.id)
        else:
            form = PostForm()
        return render(request,'blog/post_edit.html', {'form': form})
    return redirect('post_list')


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user == post.author:
        if request.method == 'POST':
                form = PostForm(request.POST, instance=post)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.author = request.user
                    post.published_date = timezone.now()
                    post.save()
                    return redirect('post_detail', id=post.id)
        else:
            form = PostForm()
        return render(request,'blog/post_edit.html', {'form': form})
    return redirect('post_list')


def post_list(request):
    posts = Post.objects.for_user(user=request.user)
    return render(request, 'blog/post_list.html', {'posts':posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    if not post.is_publish() and not request.user.is_staff:
        raise Http404("Запись в блоге не найдена")
    return render(request, 'blog/post_detail.html', {'post': post})


def handler404(request, exception, template_name="404.html"):
    response = render(None, template_name)
    response.status_code = 404
    return response
    # render_to_response устарел в Django 3.0