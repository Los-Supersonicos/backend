from rest_framework import viewsets
from rest_framework import permissions
from app.models import (
    Publication
)
from app.serializers import (
    PublicationSerializer
)


class PublicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows publications to be viewed or edited.
    """
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = [permissions.AllowAny]