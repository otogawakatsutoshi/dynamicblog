from rest_framework import filters, generics, viewsets,status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models,serializer

class TarentViewSet(APIView):
    def get(self, request, format=None):
        queryset = models.Tarent.objects.all()
        json = serializer.TarentSerializer(queryset, many=True)
        return Response(json.data)

class TarentPersonalityViewSet(APIView):
    queryset = models.TarentPersonality.objects.all()
    serializer_class = serializer.TarentPersonalitySerializer
    filter_fields = ('name',)

class TarentFaceViewSet(APIView):
    queryset = models.TarentFace.objects.all()
    serializer_class = serializer.TarentFaceSerializer
    filter_fields = ('name',)

class TarentBodyViewSet(APIView):
    queryset = models.TarentBody.objects.all()
    serializer_class = serializer.TarentBodySerializer
    filter_fields = ('name',)

class TarentUpperBodyViewSet(APIView):
    queryset = models.TarentUpperBody.objects.all()
    serializer_class = serializer.TarentUpperBodySerializer
    filter_fields = ('name',)

class TarentLowerBodyViewSet(APIView):
    queryset = models.TarentLowerBody.objects.all()
    serializer_class = serializer.TarentLowerBodySerializer
    filter_fields = ('name',)

class TarentBraSizeViewSet(APIView):
    queryset = models.TarentBraSize.objects.all()
    serializer_class = serializer.TarentBraSizeSerializer
    filter_fields = ('name',)

class AffiliateProviderViewSet(APIView):
    queryset = models.AffiliateProvider.objects.all()
    serializer_class = serializer.AffiliateProviderSerializer
    filter_fields = ('name',)

class TarentArtInfoSiteArticleViewSet(APIView):
    queryset = models.TarentArtInfoSiteArticle.objects.all()
    serializer_class = serializer.TarentArtInfoSiteArticleSerializer
    filter_fields = ('name',)

class TarentArtSampleImageViewSet(APIView):
    queryset = models.TarentArtSampleImage.objects.all()
    serializer_class = serializer.TarentArtSampleImageSerializer
    filter_fields = ('name',)

class InfoSiteViewSet(APIView):
    queryset = models.InfoSite.objects.all()
    serializer_class = serializer.InfoSiteSerializer
    filter_fields = ('name',)

class TarentArtViewSet(APIView):
    queryset = models.TarentArt.objects.all()
    serializer_class = serializer.TarentArtSerializer
    filter_fields = ('name',)

class TarentArtFetishismViewSet(APIView):
    queryset = models.TarentArtFetishism.objects.all()
    serializer_class = serializer.TarentArtFetishismSerializer
    filter_fields = ('name',)

class TarentTimelineViewSet(APIView):
    queryset = models.TarentTimeline.objects.all()
    serializer_class = serializer.TarentTimelineSerializer
    filter_fields = ('draft',)

class TarentSiteViewSet(APIView):
    queryset = models.TarentSite.objects.all()
    serializer_class = serializer.TarentSiteSerializer
    filter_fields = ('name',)

class SiteTypeViewSet(APIView):
    queryset = models.SiteType.objects.all()
    serializer_class = serializer.SiteTypeSerializer
    filter_fields = ('name',)
