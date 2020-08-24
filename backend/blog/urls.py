from rest_framework import routers
from .views import TarentTimelineViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'tarent_timeline', TarentTimelineViewSet)

urlpatterns = [
   path('', include(router.urls)),
]