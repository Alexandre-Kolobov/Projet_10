from rest_framework.serializers import ModelSerializer, SerializerMethodField, CharField, ValidationError
from suivi_projets.models import Projet, Issue, Comment, Contributor


class CommentSerializer(ModelSerializer):
    author = CharField(read_only="True")

    projet_id = SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['uuid', 'projet_id', 'issue', 'author', 'description']

    def get_projet_id(self, instance):
        return instance.issue.projet.id


class IssueListSerializer(ModelSerializer):
    author = CharField(read_only="True")

    class Meta:
        model = Issue
        fields = [
            'id',
            'projet',
            'author',
            'title',
            'description',
            'priority',
            'nature',
            'status',
            'created_time',
            'assigned_to'
            ]

    def validate_assigned_to(self, value):
        if self.instance:
            projet_id = self.instance.projet.id
        else:
            projet_id = self.initial_data.get("projet")

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
            'projet',
            'author',
            'title',
            'description',
            'priority',
            'nature',
            'status',
            'created_time',
            'assigned_to',
            'comments'
            ]


class ProjetListSerializer(ModelSerializer):
    author = CharField(read_only="True")

    class Meta:
        model = Projet
        fields = ['id', 'author', 'type', 'title', 'description', 'created_time']


class ProjetDetailSerializer(ModelSerializer):
    author = CharField(read_only="True")
    issues = IssueListSerializer(many=True, required=False)

    class Meta:
        model = Projet
        fields = ['id', 'author', 'type', 'title', 'description', 'created_time', 'contributors', 'issues']
