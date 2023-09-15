from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField, ValidationError
from suivi_projets.models import Projet, Issue, Comment, Contributor


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
        fields = [
            'id',
            'author',
            'title',
            'description',
            'priority',
            'nature',
            'status',
            'projet',
            'created_time',
            'assigned_to'
            ]

    def validate_assigned_to(self, value):
        projet_id = self.instance.projet.id
        user_id = value
        if Contributor.objects.filter(user=user_id, projet=projet_id).exists():
            return value
        else:
            raise ValidationError('You have to assigne User to the Issue only if he is a contributor of this project')


class IssueDetailSerializer(ModelSerializer):

    author = CharField(read_only="True")
    comments = CommentSerializer(many=True, required=False)

    class Meta:
        model = Issue
        fields = [
            'id',
            'author',
            'title',
            'description',
            'priority',
            'nature',
            'status',
            'projet',
            'created_time',
            'assigned_to',
            'comments'
            ]


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
