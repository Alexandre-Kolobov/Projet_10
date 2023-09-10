from django.db import models
from uuid import uuid4

class Projet(models.Model):
    TYPE_CHOICES = [
        ('BACK-END', 'back-end'),
        ('FRONT-END', 'front-end'),
        ('IOS', 'iOS'),
        ('ANDROID', 'Android'),
    ]

    title = models.fields.CharField(max_length=150)
    description = models.fields.TextField(blank=False)
    type = models.fields.CharField(max_length=20, choices=TYPE_CHOICES, default="BACK-END")
    created_time = models.fields.DateTimeField(auto_now_add=True)


class Issue(models.Model):
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]

    NATURE_CHOICES = [
        ('BUG', 'Bug'),
        ('FEATURE', 'Feature'),
        ('TASK', 'Task'),
    ]

    STATUS_CHOICES = [
        ('TO DO', 'To Do'),
        ('IN PROGRESS', 'In Progress'),
        ('FINISHED', 'Finished'),
    ]
        
    title = models.fields.CharField(max_length=150)
    description = models.fields.TextField(blank=False)
    priority = models.fields.CharField(max_length=20, choices=PRIORITY_CHOICES, default="LOW")
    nature = models.fields.CharField(max_length=20, choices=NATURE_CHOICES, default="BUG")
    status = models.fields.CharField(max_length=20, choices=STATUS_CHOICES, default="TO DO")
    projet = models.ForeignKey('Projet', on_delete=models.CASCADE, related_name="issues")
    created_time = models.fields.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    description = models.fields.TextField(blank=False)
    issue = models.ForeignKey('Issue', on_delete=models.CASCADE, related_name="comments")