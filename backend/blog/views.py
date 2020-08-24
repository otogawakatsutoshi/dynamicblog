from rest_framework import filters, generics, viewsets
from .models import Tarent,TarentPersonality,TarentFace,TarentBody,TarentUpperBody,TarentLowerBody,TarentBraSize,AffiliateProvider,TarentArtInfoSiteArticle,TarentArtSampleImage,TarentArt,TarentArtFetishism,TarentTimeline,TarentSite,SiteType,InfoSite
from .serializer import TarentSerializer,TarentPersonalitySerializer,TarentFaceSerializer,TarentBodySerializer,TarentUpperBodySerializer,TarentLowerBodySerializer,TarentBraSizeSerializer,AffiliateProviderSerializer,TarentArtInfoSiteArticleSerializer,TarentArtSampleImageSerializer,InfoSiteSerializer,TarentArtSerializer,TarentArtFetishismSerializer,TarentTimelineSerializer,TarentSiteSerializer,SiteTypeSerializer

class TarentViewSet(viewsets.ModelViewSet):
    queryset = Tarent.objects.all()
    serializer_class = TarentSerializer
    filter_fields = ('name',)

class TarentPersonalityViewSet(viewsets.ModelViewSet):
    queryset = TarentPersonality.objects.all()
    serializer_class = TarentPersonalitySerializer
    filter_fields = ('name',)

class TarentFaceViewSet(viewsets.ModelViewSet):
    queryset = TarentFace.objects.all()
    serializer_class = TarentFaceSerializer
    filter_fields = ('name',)

class TarentBodyViewSet(viewsets.ModelViewSet):
    queryset = TarentBody.objects.all()
    serializer_class = TarentBodySerializer
    filter_fields = ('name',)

class TarentUpperBodyViewSet(viewsets.ModelViewSet):
    queryset = TarentUpperBody.objects.all()
    serializer_class = TarentUpperBodySerializer
    filter_fields = ('name',)

class TarentLowerBodyViewSet(viewsets.ModelViewSet):
    queryset = TarentLowerBody.objects.all()
    serializer_class = TarentLowerBodySerializer
    filter_fields = ('name',)

class TarentBraSizeViewSet(viewsets.ModelViewSet):
    queryset = TarentBraSize.objects.all()
    serializer_class = TarentBraSizeSerializer
    filter_fields = ('name',)

class AffiliateProviderViewSet(viewsets.ModelViewSet):
    queryset = AffiliateProvider.objects.all()
    serializer_class = AffiliateProviderSerializer
    filter_fields = ('name',)

class TarentArtInfoSiteArticleViewSet(viewsets.ModelViewSet):
    queryset = TarentArtInfoSiteArticle.objects.all()
    serializer_class = TarentArtInfoSiteArticleSerializer
    filter_fields = ('name',)

class TarentArtSampleImageViewSet(viewsets.ModelViewSet):
    queryset = TarentArtSampleImage.objects.all()
    serializer_class = TarentArtSampleImageSerializer
    filter_fields = ('name',)

class InfoSiteViewSet(viewsets.ModelViewSet):
    queryset = InfoSite.objects.all()
    serializer_class = InfoSiteSerializer
    filter_fields = ('name',)

class TarentArtViewSet(viewsets.ModelViewSet):
    queryset = TarentArt.objects.all()
    serializer_class = TarentArtSerializer
    filter_fields = ('name',)

class TarentArtFetishismViewSet(viewsets.ModelViewSet):
    queryset = TarentArtFetishism.objects.all()
    serializer_class = TarentArtFetishismSerializer
    filter_fields = ('name',)

class TarentTimelineViewSet(viewsets.ModelViewSet):
    queryset = TarentTimeline.objects.all()
    serializer_class = TarentTimelineSerializer
    filter_fields = ('draft',)

class TarentSiteViewSet(viewsets.ModelViewSet):
    queryset = TarentSite.objects.all()
    serializer_class = TarentSiteSerializer
    filter_fields = ('name',)

class SiteTypeViewSet(viewsets.ModelViewSet):
    queryset = SiteType.objects.all()
    serializer_class = SiteTypeSerializer
    filter_fields = ('name',)

