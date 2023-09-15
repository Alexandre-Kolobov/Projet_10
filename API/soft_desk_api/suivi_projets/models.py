from django.conf import settings
from django.db import models
from uuid import uuid4
from authentication.models import User


class Projet(models.Model):
    TYPE_CHOICES = [
        ('BACK-END', 'back-end'),
        ('FRONT-END', 'front-end'),
        ('IOS', 'iOS'),
        ('ANDROID', 'Android'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projet_author", blank=True, null=True)
    title = models.fields.CharField(max_length=150)
    description = models.fields.TextField(blank=False)
    type = models.fields.CharField(max_length=20, choices=TYPE_CHOICES, default="BACK-END")
    created_time = models.fields.DateTimeField(auto_now_add=True)
    contributors = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Contributor')


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
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="issue_author")
    title = models.fields.CharField(max_length=150)
    description = models.fields.TextField(blank=False)
    priority = models.fields.CharField(max_length=20, choices=PRIORITY_CHOICES, default="LOW")
    nature = models.fields.CharField(max_length=20, choices=NATURE_CHOICES, default="BUG")
    status = models.fields.CharField(max_length=20, choices=STATUS_CHOICES, default="TO DO")
    projet = models.ForeignKey('Projet', on_delete=models.CASCADE, related_name="issues")
    created_time = models.fields.DateTimeField(auto_now_add=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='assigned_issues')


class Comment(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_author")
    description = models.fields.TextField(blank=False)
    issue = models.ForeignKey('Issue', on_delete=models.CASCADE, related_name="comments")


class Contributor(models.Model):
    ROLE = [
        ('AUTHOR', 'Author'),
        ('CONTRIBUTOR', 'Contributor'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    role = models.fields.CharField(max_length=20, choices=ROLE, default="Contributor")
