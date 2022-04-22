from django.db import models
from django.http import HttpResponse

# Create your models here.
class Task_free(models.Model):

    title = models.CharField('Name', max_length=50)
    task = models.TextField('Caption')
    task_img = models.ImageField(upload_to='main/static/main/img')

    def __str__(self):
        return self.title

    def image(self):
        s = f'{self.task_img}'
        s = s[4:]
        return s

    class Meta:
        verbose_name = 'Tasks'
        verbose_name_plural = 'Task'

# ----------------------------------------------------------------

class News(models.Model):

    title = models.CharField('Name', max_length=50)
    text = models.TextField('Caption news')
    date = models.DateTimeField('Date publication')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


