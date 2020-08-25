from rest_framework import routers
from . import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'tarent',views.TarentViewSet)
router.register(r'tarent_personality',views.TarentPersonalityViewSet)
router.register(r'tarent_face',views.TarentFaceViewSet)
router.register(r'tarent_body',views.TarentBodyViewSet)
router.register(r'tarent_upper_body',views.TarentUpperBodyViewSet)
router.register(r'tarent_lower_body',views.TarentLowerBodyViewSet)
router.register(r'tarent_bra_size',views.TarentBraSizeViewSet)
router.register(r'affiliate_provider',views.AffiliateProviderViewSet)
router.register(r'tarent_art_infoSite_article',views.TarentArtInfoSiteArticleViewSet)
router.register(r'tarent_art_sample_image',views.TarentArtSampleImageViewSet)
router.register(r'info_site',views.InfoSiteViewSet)
router.register(r'tarent_art',views.TarentArtViewSet)
router.register(r'tarent_art_fetishism',views.TarentArtFetishismViewSet)
router.register(r'tarent_timeline',views.TarentTimelineViewSet)
router.register(r'tarent_site',views.TarentSiteViewSet)
router.register(r'site_type',views.SiteTypeViewSet)

urlpatterns = [
   path('', include(router.urls)),
]