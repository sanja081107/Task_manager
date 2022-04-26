from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('Name', max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):

    title = models.CharField('Name', max_length=50)
    text = models.TextField('Caption news')
    categories = models.ManyToManyField(Category, related_name='posts')
    created = models.DateTimeField('Date publication', auto_now_add=True)
    edit = models.DateTimeField('Date edit', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class Comment(models.Model):
    author = models.CharField(max_length=50)
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
