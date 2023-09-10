Endpoints (GET):
    1) api/projets/
    2) api/projets/<projet.id>
    3) api/issues/
    4) api/issues/<issue.id>
    5) api/comments/
    6) api/comments/<comment.id>

Endpoints (POST):
    api/projets/
    api/issues/
    api/comments/

Endpoints (PUT):
    api/projets/<projet.id>
    api/issues/<issue.id>
    api/comments/<comment.id>

Endpoints (DELETE):
    api/projets/<projet.id>
    api/issues/<issue.id>
    api/comments/<comment.id>



Filters:
    projet_id:
        api/issues/?projet_id=
        api/comments/?projet_id=
    
    issue_id:
        api/comments/?issue_id=