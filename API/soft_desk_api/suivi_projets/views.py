from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.viewsets import ModelViewSet
from suivi_projets.models import Projet, Issue, Comment, Contributor
from authentication.models import User
from suivi_projets.serializers import IssueListSerializer, IssueDetailSerializer, ProjetListSerializer, ProjetDetailSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError


class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProjetViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):
    serializer_class = ProjetListSerializer
    detail_serializer_class = ProjetDetailSerializer
    permission_classes = [IsAuthenticated]
        
    def get_queryset(self):
        queryset = Projet.objects.all()
        return queryset
    
    @transaction.atomic
    @action(detail=False, methods=['post'])
    def creer_projet(self, request):
        serializer = ProjetListSerializer(data=request.data)
        if serializer.is_valid():
            projet = serializer.save()

            user = User.objects.get(pk=request.user.id)
            contributor = Contributor(user=user, projet=projet, role='AUTHOR')
            contributor.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    @transaction.atomic
    @action(detail=True, methods=['post'])
    def suivre_projet(self, request, pk):
        projet = get_object_or_404(Projet, pk=pk)
        user = User.objects.get(pk=request.user.id)

        if Contributor.objects.filter(user=user, projet=projet).exists():
            raise ValidationError("Contributor already exists for this user and project")
        contributor = Contributor(user=user, projet=projet, role='CONTRIBUTOR')
        contributor.save()

        return Response({"message": "You was added as contributor"}, status=status.HTTP_201_CREATED)


class IssueViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):
    serializer_class = IssueListSerializer
    detail_serializer_class = IssueDetailSerializer
        
    def get_queryset(self):
        queryset = Issue.objects.all()
        projet_id = self.request.GET.get('projet_id')
        if projet_id is not None:
            queryset = queryset.filter(projet_id=projet_id)

        return queryset

    
class CommentViewset(ReadOnlyModelViewSet):
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