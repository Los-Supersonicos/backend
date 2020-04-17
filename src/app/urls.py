from django.urls import include, path
from rest_framework import routers
from django.contrib import admin
from app import views

router = routers.DefaultRouter()
router.register(r'publications', views.PublicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(r'admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]