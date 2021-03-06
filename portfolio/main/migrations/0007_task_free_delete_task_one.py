# Generated by Django 4.0.3 on 2022-04-18 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_task_one_delete_task_new'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task_free',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Name')),
                ('task', models.TextField(verbose_name='Caption')),
                ('image', models.FileField(upload_to='main/static/main/img/')),
            ],
            options={
                'verbose_name': 'Tasks',
                'verbose_name_plural': 'Task',
            },
        ),
        migrations.DeleteModel(
            name='Task_one',
        ),
    ]
