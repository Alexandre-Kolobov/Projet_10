# Generated by Django 4.2.4 on 2023-09-08 15:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('suivi_projets', '0002_projet_created_time_projet_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('priority', models.CharField(choices=[('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')], default='LOW', max_length=20)),
                ('nature', models.CharField(choices=[('BUG', 'Bug'), ('FEATURE', 'Feature'), ('TASK', 'Task')], default='BUG', max_length=20)),
                ('status', models.CharField(choices=[('TO DO', 'To Do'), ('IN PROGRESS', 'In Progress'), ('FINISHED', 'Finished')], default='TO DO', max_length=20)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('projet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='suivi_projets.projet')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField()),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='suivi_projets.issue')),
            ],
        ),
    ]