from django.contrib import admin
from suivi_projets.models import Projet, Issue, Comment


class ProjetAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'description', 'type', 'created_time')


class IssueAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'description', 'priority', 'nature', 'status', 'projet', 'created_time')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'author', 'description', 'issue')


admin.site.register(Projet, ProjetAdmin)
admin.site.register(Issue, IssueAdmin)
admin.site.register(Comment, CommentAdmin)
