from django.conf.urls import url, include
from rest_framework import routers
from .views import BoardViewSet, ThreadViewSet, UserViewSet, PostViewSet, ParticipantViewSet

# DRF router for REST API viewsets
router = routers.DefaultRouter()

# Register endpoints with DRF router
router.register(r'boards', BoardViewSet, r"board")
router.register(r'threads', ThreadViewSet, r"thread")
router.register(r'Users', UserViewSet, r"User")
router.register(r'Posts', PostViewSet, r"Post")
router.register(r'Participants', ParticipantViewSet, r"Participant")

urlpatterns = [
    url(r'^', include(router.urls, namespace='api')),
    url(r'^', include('rest_framework.urls', namespace='rest_framework')), # Login/Logout URLs
]
