from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('project_tasks', views.project_tasks, name='project_tasks'),
    path('about_us', views.about_us, name='about_us'),
    path('create_task', views.create_task, name='create_task'),
    path('create_news', views.create_news, name='create_news'),
    path('project_news', views.project_news, name='project_news'),
    path('<int:pk>', views.project_detail_task, name='project_detail_task'),
    path('<int:pk>/delete', views.TaskDeleteView.as_view(), name='delete_task'),
    path('<int:pk>/update', views.TaskUpdateView.as_view(), name='update_task')
]
