from rest_framework.viewsets import ModelViewSet
from suivi_projets.models import Projet, Issue, Comment, Contributor
from authentication.models import User
from suivi_projets.serializers import (
    IssueListSerializer,
    IssueDetailSerializer,
    ProjetListSerializer,
    ProjetDetailSerializer,
    CommentSerializer
)
from django.db import transaction
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError
from suivi_projets.permissions import (
    IsProjetAuthorOrContributor,
    IsIssueAuthorOrContributor,
    IsCommentAuthorOrContributor
)


class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProjetViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = ProjetListSerializer
    detail_serializer_class = ProjetDetailSerializer
    permission_classes = [IsProjetAuthorOrContributor]

    def get_queryset(self):
        queryset = Projet.objects.all()
        return queryset

    def perform_create(self, serializer):
        projet = serializer.save(author=self.request.user)
        contributor = Contributor(user=self.request.user, projet=projet, role='AUTHOR')
        contributor.save()

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


class IssueViewset(MultipleSerializerMixin, ModelViewSet):
    serializer_class = IssueListSerializer
    detail_serializer_class = IssueDetailSerializer
    permission_classes = [IsIssueAuthorOrContributor]

    def get_queryset(self):
        user_projets = Projet.objects.filter(contributors=self.request.user)
        queryset = Issue.objects.filter(projet__in=user_projets)

        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsCommentAuthorOrContributor]

    def get_queryset(self):
        queryset = Comment.objects.all()
        user_projets = Projet.objects.filter(contributors=self.request.user)
        user_issues = Issue.objects.filter(projet__in=user_projets)
        queryset = Comment.objects.filter(issue__in=user_issues)

        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
