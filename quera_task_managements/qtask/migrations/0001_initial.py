# Generated by Django 4.2.5 on 2023-09-07 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_first_name', models.CharField(max_length=50)),
                ('owner_last_name', models.CharField(max_length=50)),
                ('owner_email', models.EmailField(max_length=254)),
                ('owner_team_role', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('project_manager', models.ForeignKey(default='Matin himself', on_delete=django.db.models.deletion.DO_NOTHING, to='qtask.owner')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_title', models.CharField(max_length=100)),
                ('task_descriptions', models.CharField(blank=True, max_length=200)),
                ('task_priority', models.CharField(choices=[('HOT FIX', 'Hot'), ('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=20)),
                ('task_created_time', models.DateTimeField(auto_now_add=True)),
                ('task_deadline', models.DateTimeField()),
                ('task_blongs_to_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qtask.project')),
                ('task_owners', models.ManyToManyField(to='qtask.owner')),
            ],
        ),
    ]
