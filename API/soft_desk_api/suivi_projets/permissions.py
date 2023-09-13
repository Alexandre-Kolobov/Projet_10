from rest_framework.permissions import BasePermission
from authentication.models import User
from suivi_projets.models import Contributor, Issue, Comment, Projet
from django.shortcuts import get_object_or_404


class IsProjetAuthorOrContributor(BasePermission):

    def has_permission(self, request, view):
        if view.action == "list":
            return bool(request.user and request.user.is_authenticated)
        
        if view.action == "retrieve":
            project_id = view.kwargs.get('pk')
            user = request.user

            try:
                contributor = user.projet_set.filter(id=project_id).exists()
            except:
                return False
            return bool(request.user and request.user.is_authenticated and contributor)
        
        if view.action == "update" or view.action == "partial_update" or view.action == "destroy":
            project_id = view.kwargs.get('pk')

            try:
                contributor = Contributor.objects.get(user=request.user, projet=project_id)
            except:
                return False
            
            return bool(request.user and request.user.is_authenticated and contributor.role == "AUTHOR")
    
        return bool(request.user and request.user.is_authenticated)


class IsIssueAuthorOrContributor(BasePermission):

    def has_permission(self, request, view):
        if view.action == "list":
            return bool(request.user and request.user.is_authenticated)
        
        if view.action == "retrieve":
            issue_id = view.kwargs.get('pk')
            user = request.user
            
            try:
                issue = Issue.objects.get(pk=issue_id)
            except:
                return False
        
            try:
                contributor = user.projet_set.filter(id=issue.projet.id).exists()
            except:
                return False
            
            return bool(request.user and request.user.is_authenticated and contributor)
        
        if view.action == "update" or view.action == "partial_update" or view.action == "destroy":
            issue_id = view.kwargs.get('pk')
            author = Issue.objects.get(pk=issue_id).author
            return bool(request.user and request.user.is_authenticated and request.user.id == author.id)
    
        return bool(request.user and request.user.is_authenticated)
    
class IsCommentAuthorOrContributor(BasePermission):

    def has_permission(self, request, view):
        if view.action == "list":
            return bool(request.user and request.user.is_authenticated)
        
        if view.action == "retrieve":
            comment_id = view.kwargs.get('pk')
            user = request.user
            
            try:
                comment = Comment.objects.get(pk=comment_id)
            except:
                return False
        
            try:
                contributor = user.projet_set.filter(id=comment.issue.projet.id).exists()
            except:
                return False
            
            return bool(request.user and request.user.is_authenticated and contributor)
        
        if view.action == "update" or view.action == "partial_update" or view.action == "destroy":
            comment_id = view.kwargs.get('pk')
            author = Comment.objects.get(pk=comment_id).author
            return bool(request.user and request.user.is_authenticated and request.user.id == author.id)
    
        return bool(request.user and request.user.is_authenticated)