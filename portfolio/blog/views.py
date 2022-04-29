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

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/create_blog.html'
    form_class = PostForm


# class CommentDeleteView(DeleteView):
#     model = Comment
#     pk = model
#     template_name = 'blog/delete_comment.html'
#     success_url = '/blog'


def comment_delete(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == 'POST':
        comment.delete()
        return redirect(f'/blog{comment.post.pk}/detail_blog')
    return render(request, 'blog/delete_comment.html')


def detail_blog(request, pk):
    post = Post.objects.get(pk=pk)
    comment = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comment': comment,
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
            return redirect(f'/blog{post.id}/detail_blog')
        else:
            error = 'error'

    form = CommentForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'blog/comment_blog.html', context)
