# Generated by Django 4.2.4 on 2023-09-10 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('suivi_projets', '0004_comment_projet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='projet',
        ),
    ]