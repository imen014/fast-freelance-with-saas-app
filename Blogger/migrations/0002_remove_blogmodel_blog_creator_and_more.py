# Generated by Django 5.1.2 on 2024-10-24 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blogger', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmodel',
            name='blog_creator',
        ),
        migrations.RemoveField(
            model_name='imagemodel',
            name='uploader',
        ),
    ]
