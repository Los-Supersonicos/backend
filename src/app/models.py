from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.gis.db import models as gismodels


class Publication(models.Model):
    """A publication can be shown in a map."""

    PUBLICATION_TYPES = [
        ('N', 'Need'),
        ('O', 'Offer')
    ]

    type = models.CharField(max_length=1, choices=PUBLICATION_TYPES)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now=True)
    location = gismodels.PointField()
    description = models.TextField()
