from rest_framework.serializers import ModelSerializer, SerializerMethodField
from suivi_projets.models import Projet, Issue, Comment

class CommentSerializer(ModelSerializer):

    projet_id = SerializerMethodField()
 
    class Meta:
        model = Comment
        fields = ['uuid', 'description', 'projet_id', 'issue']

    def get_projet_id(self, instance):
        return instance.issue.projet.id


class IssueListSerializer(ModelSerializer):

    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'priority', 'nature', 'status', 'projet', 'created_time']


class IssueDetailSerializer(ModelSerializer):

    comments = CommentSerializer(many=True, required=False)

    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'priority', 'nature', 'status', 'projet', 'created_time', 'comments']


class ProjetListSerializer(ModelSerializer):

    class Meta:
        model = Projet
        fields = ['id', 'title', 'description', 'type', 'created_time']


class ProjetDetailSerializer(ModelSerializer):

    issues = IssueListSerializer(many=True, required=False)
 
    class Meta:
        model = Projet
        fields = ['id', 'title', 'description', 'type', 'created_time', 'issues']


