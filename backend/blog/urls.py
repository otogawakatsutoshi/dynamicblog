from rest_framework import routers
from .views import TarentViewSet,TarentPersonalityViewSet,TarentFaceViewSet,TarentBodyViewSet,TarentUpperBodyViewSet,TarentLowerBodyViewSet,TarentBraSizeViewSet,AffiliateProviderViewSet,TarentArtInfoSiteArticleViewSet,TarentArtSampleImageViewSet,InfoSiteViewSet,TarentArtViewSet,TarentArtFetishismViewSet,TarentTimelineViewSet,TarentSiteViewSet,SiteTypeViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'tarent',TarentViewSet)
router.register(r'tarent_personality',TarentPersonalityViewSet)
router.register(r'tarent_face',TarentFaceViewSet)
router.register(r'tarent_body',TarentBodyViewSet)
router.register(r'tarent_upper_body',TarentUpperBodyViewSet)
router.register(r'tarent_lower_body',TarentLowerBodyViewSet)
router.register(r'tarent_bra_size',TarentBraSizeViewSet)
router.register(r'affiliate_provider',AffiliateProviderViewSet)
router.register(r'tarent_art_infoSite_article',TarentArtInfoSiteArticleViewSet)
router.register(r'tarent_art_sample_image',TarentArtSampleImageViewSet)
router.register(r'info_site',InfoSiteViewSet)
router.register(r'tarent_art',TarentArtViewSet)
router.register(r'tarent_art_fetishism',TarentArtFetishismViewSet)
router.register(r'tarent_timeline',TarentTimelineViewSet)
router.register(r'tarent_site',TarentSiteViewSet)
router.register(r'site_type',SiteTypeViewSet)

urlpatterns = [
   path('', include(router.urls)),
]