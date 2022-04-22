from django.shortcuts import render, redirect
from .models import Task_free, News
from .forms import Task_freeForm, NewsForm
from django.views.generic import UpdateView, DeleteView
# Create your views here.
# ------------------------------------------------------
def home(request):
    return render(request, 'main/home.html', {'title': 'Home page'})
# ------------------------------------------------------
def project_tasks(request):
    task = Task_free.objects.order_by('-id')
    context = {'task': task,
               'title': 'Tasks'}
    return render(request, 'main/project_tasks.html', context)
# ------------------------------------------------------
def project_detail_task(request, pk):
    task = Task_free.objects.get(pk=pk)
    context = {'task': task,
               'title': 'Detail task page'}
    return render(request, 'main/project_detail_task.html', context)
# ------------------------------------------------------
def about_us(request):
    return render(request, 'main/about_us.html')
# ------------------------------------------------------
def create_task(request):
    error = ''
    if request.method == 'POST':
        form = Task_freeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'input again'
    form = Task_freeForm()
    context = {
        'form': form,
        'error': error,
        'title': 'Create task'
    }
    return render(request, 'main/create_task.html', context)
# ------------------------------------------------------

class TaskDeleteView(DeleteView):
    model = Task_free
    template_name = 'main/delete_task.html'
    context_object_name = 'task'
    success_url = '/project_tasks'

class TaskUpdateView(UpdateView):
    pass

# ------------------------------------------------------
def create_news(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Error'

    form = NewsForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'main/create_news.html', context)
# ------------------------------------------------------
def project_news(request):
    news = News.objects.order_by('-date')
    context = {
        'news': news,
    }
    return render(request, 'main/project_news.html', context)
