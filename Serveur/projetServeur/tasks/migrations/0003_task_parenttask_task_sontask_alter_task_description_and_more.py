# Generated by Django 5.2 on 2025-04-10 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_remove_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='parentTask',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='task',
            name='sonTask',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='statut',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(default='none', max_length=200),
        ),
    ]
