from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from django.urls import path, include

urlpatterns = [
    path('tarent/<int:id>/', views.TarentViewSet.as_view()),
    path('tarent_personality/', views.TarentPersonalityViewSet.as_view()),
    path('tarent_face/<int:id>/', views.TarentFaceViewSet.as_view()),
    path('tarent_body/', views.TarentBodyViewSet.as_view()),
    path('tarent_upper_body/', views.TarentUpperBodyViewSet.as_view()),
    path('tarent_lower_body/', views.TarentLowerBodyViewSet.as_view()),
    path('tarent_bra_size/<int:id>/', views.TarentBraSizeViewSet.as_view()),
    path('affiliate_provider/', views.AffiliateProviderViewSet.as_view()),
    path('tarent_art_info_site_article/', views.TarentArtInfoSiteArticleViewSet.as_view()),
    path('tarent_art_sample_image/', views.TarentArtSampleImageViewSet.as_view()),
    path('info_site/', views.InfoSiteViewSet.as_view()),
    path('tarent_art/', views.TarentArtViewSet.as_view()),
    path('tarent_art_fetishism/', views.TarentArtFetishismViewSet.as_view()),
    path('tarent_timeline/', views.TarentTimelineViewSet.as_view()),
    path('tarent_timeline/<tarent_id>/', views.TarentTimelineViewSet.as_view()),
    path('tarent_site/', views.TarentSiteViewSet.as_view()),
    path('site_type/', views.SiteTypeViewSet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)