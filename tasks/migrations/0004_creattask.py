# Generated by Django 5.2 on 2025-04-10 07:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_parenttask_task_sontask_alter_task_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreatTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subtask', to='tasks.creattask')),
                ('assignedTeams', models.ManyToManyField(to='tasks.team')),
                ('assignedUsers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('createdby', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='createdTasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
