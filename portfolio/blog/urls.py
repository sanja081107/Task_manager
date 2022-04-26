from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog'),
    path('create_blog', views.create_blog, name='create_blog'),
    path('<int:pk>/delete_blog', views.BlogDeleteView.as_view(), name='delete_blog'),
    path('<int:pk>/detail_blog', views.detail_blog, name='detail_blog'),
    path('<int:pk>/comment_blog', views.comment_blog, name='comment_blog'),
]
