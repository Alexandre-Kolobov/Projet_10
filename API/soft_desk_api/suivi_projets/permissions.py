from rest_framework.permissions import BasePermission
from suivi_projets.models import Contributor, Issue, Comment, Projet


class IsProjetAuthorOrContributor(BasePermission):

    def has_permission(self, request, view):
        if view.action == "list":
            return bool(request.user and request.user.is_authenticated)

        if view.action == "retrieve":
            self.message = "You have to be contibutor to see details of this project"
            project_id = view.kwargs.get('pk')
            user = request.user

            try:
                Projet.objects.get(pk=project_id)
            except Projet.DoesNotExist:
                self.message = "Projet with this id doesn't exist"
                return False

            try:
                contributor = user.projet_set.filter(id=project_id).exists()
            except user.DoesNotExist:
                return False
            return bool(request.user and request.user.is_authenticated and contributor)

        if view.action == "update" or view.action == "partial_update" or view.action == "destroy":
            self.message = "You have to be the author to update or delete this project"
            project_id = view.kwargs.get('pk')

            try:
                Projet.objects.get(pk=project_id)
            except Projet.DoesNotExist:
                self.message = "Projet with this id doesn't exist"
                return False

            try:
                contributor = Contributor.objects.get(user=request.user, projet=project_id)
            except Contributor.DoesNotExist:
                return False

            return bool(request.user and request.user.is_authenticated and contributor.role == "AUTHOR")

        return bool(request.user and request.user.is_authenticated)


class IsIssueAuthorOrContributor(BasePermission):

    def has_permission(self, request, view):
        if view.action == "list":
            self.message = "You have to be a contibutor to see issues and comments"
            return bool(request.user and request.user.is_authenticated)

        if view.action == "retrieve":
            self.message = "You have to be a contibutor to see details of this issue"
            issue_id = view.kwargs.get('pk')
            user = request.user

            try:
                issue = Issue.objects.get(pk=issue_id)
            except Issue.DoesNotExist:
                self.message = "Issue with this id doesn't exist"
                return False

            try:
                contributor = user.projet_set.filter(id=issue.projet.id).exists()
            except user.DoesNotExist:
                return False

            return bool(request.user and request.user.is_authenticated and contributor)

        if view.action == "update" or view.action == "partial_update" or view.action == "destroy":
            self.message = "You have to be the author to update or delete this issue"
            issue_id = view.kwargs.get('pk')

            try:
                issue = Issue.objects.get(pk=issue_id)
            except Issue.DoesNotExist:
                self.message = "Issue with this id doesn't exist"
                return False

            author = Issue.objects.get(pk=issue_id).author
            return bool(request.user and request.user.is_authenticated and request.user.id == author.id)

        return bool(request.user and request.user.is_authenticated)


class IsCommentAuthorOrContributor(BasePermission):

    def has_permission(self, request, view):
        if view.action == "list":
            self.message = "You have to be a contibutor to see issues and comments"
            return bool(request.user and request.user.is_authenticated)

        if view.action == "retrieve":
            self.message = "You have to be a contibutor to see details of this comment"
            comment_id = view.kwargs.get('pk')
            user = request.user

            try:
                comment = Comment.objects.get(pk=comment_id)
            except Comment.DoesNotExist:
                self.message = "Comment with this id doesn't exist"
                return False

            try:
                contributor = user.projet_set.filter(id=comment.issue.projet.id).exists()
            except user.DoesNotExist:
                return False

            return bool(request.user and request.user.is_authenticated and contributor)

        if view.action == "update" or view.action == "partial_update" or view.action == "destroy":
            self.message = "You have to be the author to update or delete this comment"
            comment_id = view.kwargs.get('pk')

            try:
                comment = Comment.objects.get(pk=comment_id)
            except Comment.DoesNotExist:
                self.message = "Comment with this id doesn't exist"
                return False

            author = Comment.objects.get(pk=comment_id).author
            return bool(request.user and request.user.is_authenticated and request.user.id == author.id)

        return bool(request.user and request.user.is_authenticated)
