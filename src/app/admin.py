from django.contrib.gis import admin as admin
from app.models import Publication


class PublicationAdmin(admin.GeoModelAdmin):
    list_display = ('type', 'pub_date', 'active', 'location', 'description')


admin.site.register(Publication, PublicationAdmin)
