from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField
from suivi_projets.models import Projet, Issue, Comment


class CommentSerializer(ModelSerializer):
    author = CharField(read_only="True")

    projet_id = SerializerMethodField()
 
    class Meta:
        model = Comment
        fields = ['uuid', 'author', 'description', 'projet_id', 'issue']

    def get_projet_id(self, instance):
        return instance.issue.projet.id


class IssueListSerializer(ModelSerializer):
    author = CharField(read_only="True")

    class Meta:
        model = Issue
        fields = ['id', 'author', 'title', 'description', 'priority', 'nature', 'status', 'projet', 'created_time']


class IssueDetailSerializer(ModelSerializer):
    
    author = CharField(read_only="True")
    comments = CommentSerializer(many=True, required=False)

    class Meta:
        model = Issue
        fields = ['id', 'author', 'title', 'description', 'priority', 'nature', 'status', 'projet', 'created_time', 'comments']


class ProjetListSerializer(ModelSerializer):
    author = CharField(read_only="True")
    class Meta:
        model = Projet
        fields = ['id', 'author', 'title', 'description', 'type', 'created_time']


class ProjetDetailSerializer(ModelSerializer):
    author = CharField(read_only="True")
    issues = IssueListSerializer(many=True, required=False)
 
    class Meta:
        model = Projet
        fields = ['id', 'author', 'title', 'description', 'type', 'created_time', 'issues', 'contributors']



