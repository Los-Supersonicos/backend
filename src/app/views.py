from app.models import Publication
from app.serializers import PublicationSerializer, UserSerializer
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from rest_framework import permissions, viewsets


class PublicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows publications to be viewed or edited.
    """

    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        """
        filter by `lat`, `long` and `distance` in meters
        """
        queryset = Publication.objects.all()

        latitude = self.request.query_params.get("lat", None)
        longitude = self.request.query_params.get("long", None)
        distance = self.request.query_params.get("distance", None)

        if latitude and longitude:
            if not distance:
                distance = settings.MAX_DISTANCE_METERS
            try:
                point = Point(float(latitude), float(longitude))
            except (ValueError, TypeError):
                pass
            else:
                queryset = Publication.objects.filter(location__distance_lte=(point, D(meter=distance)))

        return queryset


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
