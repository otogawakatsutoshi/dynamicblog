from rest_framework import filters, generics, viewsets
from . import models,serializer

class TarentViewSet(viewsets.ModelViewSet):
    queryset = models.Tarent.objects.all()
    serializer_class = serializer.TarentSerializer
    filter_fields = ('name',)
    def get(self, request):
        if "id" in request.GET:
            # query_paramが指定されている場合の処理
            id = request.GET.get("id")
            TarentViewSet.queryset = models.Tarent.objects.filter(id=id)
        else:
            pass

class TarentPersonalityViewSet(viewsets.ModelViewSet):
    queryset = models.TarentPersonality.objects.all()
    serializer_class = serializer.TarentPersonalitySerializer
    filter_fields = ('name',)

class TarentFaceViewSet(viewsets.ModelViewSet):
    queryset = models.TarentFace.objects.all()
    serializer_class = serializer.TarentFaceSerializer
    filter_fields = ('name',)

class TarentBodyViewSet(viewsets.ModelViewSet):
    queryset = models.TarentBody.objects.all()
    serializer_class = serializer.TarentBodySerializer
    filter_fields = ('name',)

class TarentUpperBodyViewSet(viewsets.ModelViewSet):
    queryset = models.TarentUpperBody.objects.all()
    serializer_class = serializer.TarentUpperBodySerializer
    filter_fields = ('name',)

class TarentLowerBodyViewSet(viewsets.ModelViewSet):
    queryset = models.TarentLowerBody.objects.all()
    serializer_class = serializer.TarentLowerBodySerializer
    filter_fields = ('name',)

class TarentBraSizeViewSet(viewsets.ModelViewSet):
    queryset = models.TarentBraSize.objects.all()
    serializer_class = serializer.TarentBraSizeSerializer
    filter_fields = ('name',)

class AffiliateProviderViewSet(viewsets.ModelViewSet):
    queryset = models.AffiliateProvider.objects.all()
    serializer_class = serializer.AffiliateProviderSerializer
    filter_fields = ('name',)

class TarentArtInfoSiteArticleViewSet(viewsets.ModelViewSet):
    queryset = models.TarentArtInfoSiteArticle.objects.all()
    serializer_class = serializer.TarentArtInfoSiteArticleSerializer
    filter_fields = ('name',)

class TarentArtSampleImageViewSet(viewsets.ModelViewSet):
    queryset = models.TarentArtSampleImage.objects.all()
    serializer_class = serializer.TarentArtSampleImageSerializer
    filter_fields = ('name',)

class InfoSiteViewSet(viewsets.ModelViewSet):
    queryset = models.InfoSite.objects.all()
    serializer_class = serializer.InfoSiteSerializer
    filter_fields = ('name',)

class TarentArtViewSet(viewsets.ModelViewSet):
    queryset = models.TarentArt.objects.all()
    serializer_class = serializer.TarentArtSerializer
    filter_fields = ('name',)

class TarentArtFetishismViewSet(viewsets.ModelViewSet):
    queryset = models.TarentArtFetishism.objects.all()
    serializer_class = serializer.TarentArtFetishismSerializer
    filter_fields = ('name',)

class TarentTimelineViewSet(viewsets.ModelViewSet):
    queryset = models.TarentTimeline.objects.all()
    serializer_class = serializer.TarentTimelineSerializer
    filter_fields = ('draft',)

class TarentSiteViewSet(viewsets.ModelViewSet):
    queryset = models.TarentSite.objects.all()
    serializer_class = serializer.TarentSiteSerializer
    filter_fields = ('name',)

class SiteTypeViewSet(viewsets.ModelViewSet):
    queryset = models.SiteType.objects.all()
    serializer_class = serializer.SiteTypeSerializer
    filter_fields = ('name',)
