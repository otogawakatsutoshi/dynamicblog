from django.contrib import admin
from . import models
from guardian.admin import GuardedModelAdmin

@admin.register(models.Tarent)
class Tarent(GuardedModelAdmin):
    search_fields = ['stage_name']
   
@admin.register(models.TarentPersonality)
class TarentPersonality(GuardedModelAdmin):
    pass

@admin.register(models.TarentFace)
class TarentFace(GuardedModelAdmin):
    pass

@admin.register(models.TarentBody)
class TarentBody(GuardedModelAdmin):
    pass

@admin.register(models.TarentUpperBody)
class TarentUpperBody(GuardedModelAdmin):
    pass

@admin.register(models.TarentLowerBody)
class TarentLowerBody(GuardedModelAdmin):
    pass

@admin.register(models.TarentBraSize)
class TarentBraSize(GuardedModelAdmin):
    pass

@admin.register(models.TarentArtInfoSiteArticle)
class TarentArtInfoSiteArticle(GuardedModelAdmin):
    autocomplete_fields = ['tarent_art']

@admin.register(models.TarentArt)
class TarentArt(GuardedModelAdmin):
    search_fields = ['name']
    autocomplete_fields = ['tarent']

@admin.register(models.AffiliateProvider)
class AffiliateProvider(GuardedModelAdmin):
    pass

@admin.register(models.TarentArtSampleImage)
class TarentArtSampleImage(GuardedModelAdmin):
    search_fields = ['tarent_art']
    autocomplete_fields = ['tarent_art']

@admin.register(models.TarentArtFetishism)
class TarentArtFetishism(GuardedModelAdmin):
    pass

@admin.register(models.TarentTimeline)
class TarentTimeline(GuardedModelAdmin):
    autocomplete_fields = ['tarent']

@admin.register(models.TarentSite)
class TarentSite(GuardedModelAdmin):
    autocomplete_fields = ['tarent']

@admin.register(models.SiteType)
class SiteType(GuardedModelAdmin):
    pass

@admin.register(models.InfoSite)
class InfoSite(GuardedModelAdmin):
    pass