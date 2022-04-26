from django.shortcuts import render, redirect
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm
from django.views.generic import UpdateView, DeleteView


# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-id')
    context = {
        'posts': posts,
        'title': 'Blog page'
    }
    return render(request, 'blog/home.html', context)


def create_blog(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
        else:
            error = 'Form is not correct'

    form = PostForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'blog/create_blog.html', context)


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/delete_blog.html'
    context_object_name = 'blog'
    success_url = '/blog'


def detail_blog(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
        'title': 'Detail blog page'
    }
    return render(request, 'blog/detail_blog.html', context)


def comment_blog(request, pk):
    error = ''

    post = Post.objects.get(pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post,
            )
            comment.save()
            return redirect('blog')
        else:
            error = 'error'

    form = CommentForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'blog/comment_blog.html', context)
