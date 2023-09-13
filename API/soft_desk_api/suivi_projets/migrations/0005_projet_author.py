# Generated by Django 4.2.5 on 2023-09-13 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('suivi_projets', '0004_comment_author_issue_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='projet',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='projet_author', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
