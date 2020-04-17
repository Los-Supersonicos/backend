from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from app.models import (
    Publication
)


class PublicationSerializer(GeoFeatureModelSerializer):
    """A publication serializer."""

    class Meta:
        model = Publication
        geo_field = "location"
        fields = ('description', 'type', 'pub_date', 'active')

