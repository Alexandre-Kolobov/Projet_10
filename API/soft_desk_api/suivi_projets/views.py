from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.viewsets import ModelViewSet
 
from suivi_projets.models import Projet, Issue, Comment
from suivi_projets.serializers import IssueSerializer, ProjetSerializer, CommentSerializer
 
class ProjetViewset(ModelViewSet):
    serializer_class = ProjetSerializer
        
    def get_queryset(self):
        queryset = Projet.objects.all()
        return queryset

class IssueViewset(ModelViewSet):
    serializer_class = IssueSerializer
        
    def get_queryset(self):
        queryset = Issue.objects.all()
        projet_id = self.request.GET.get('projet_id')
        if projet_id is not None:
            queryset = queryset.filter(projet_id=projet_id)

        return queryset
    
class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer
        
    def get_queryset(self):
        queryset = Comment.objects.all()
        projet_id = self.request.GET.get('projet_id')
        if projet_id is not None:
            queryset = queryset.filter(issue__projet_id=projet_id)
        
        issue_id = self.request.GET.get('issue_id')
        if issue_id is not None:
            queryset = queryset.filter(issue_id=issue_id)

        return queryset