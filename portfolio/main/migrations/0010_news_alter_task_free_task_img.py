# Generated by Django 4.0.3 on 2022-04-21 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_task_free_delete_task_fre'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Name')),
                ('text', models.TextField(verbose_name='Caption news')),
                ('date', models.DateTimeField(verbose_name='Date publication')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
        migrations.AlterField(
            model_name='task_free',
            name='task_img',
            field=models.ImageField(upload_to='main/static/main/img'),
        ),
    ]
