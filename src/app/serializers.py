from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from app.models import (
    Publication
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username']


class PublicationSerializer(GeoFeatureModelSerializer):
    """A publication serializer."""
    user = UserSerializer(read_only=True)

    class Meta:
        model = Publication
        geo_field = "location"
        fields = ('description', 'type', 'pub_date', 'active', 'user')

