from .models import Task_free, News
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import ModelForm, TextInput, Textarea, FileInput, DateTimeInput
from django import forms

class Task_freeForm(ModelForm):
    class Meta:
        model = Task_free
        fields = ['title', 'task', 'task_img']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input name'
            }),
            'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Input task'
            }),
            'task_img': FileInput(attrs={
                'type': 'file',
                'accept': 'image/*'
            })
        }
# ----------------------------------------------------------------

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'text', 'date']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Input name'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Input news'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            })
        }
