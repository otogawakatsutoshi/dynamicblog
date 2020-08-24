from rest_framework import filters, generics, viewsets
from .models import TarentTimeline
from .serializer import TarentTimelineSerializer

class TarentTimelineViewSet(viewsets.ModelViewSet):
   queryset = TarentTimeline.objects.all()
   serializer_class = TarentTimelineSerializer
   filter_fields = ('draft',)
