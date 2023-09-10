# Generated by Django 4.2.4 on 2023-09-08 09:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('suivi_projets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projet',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projet',
            name='type',
            field=models.CharField(choices=[('BACK-END', 'back-end'), ('FRONT-END', 'front-end'), ('IOS', 'iOS'), ('ANDROID', 'Android')], default='BACK-END', max_length=20),
        ),
    ]
