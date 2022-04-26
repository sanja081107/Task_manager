from .models import Post, Comment
from django.forms import ModelForm, TextInput, Textarea, Select

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'categories']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input name'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Input text'
            })
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'body']
        widgets = {
            'author': TextInput(attrs={'placeholder': 'Input author'}),
            'body': Textarea(attrs={'placeholder': 'Input comment'}),
        }
