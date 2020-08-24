from django.contrib import admin
from .models import Tarent,TarentPersonality,TarentFace,TarentBody,TarentUpperBody,TarentLowerBody,TarentBraSize,AffiliateProvider,TarentArtInfoSiteArticle,TarentArtSampleImage,TarentArt,TarentArtFetishism,TarentTimeline,TarentSite,SiteType,InfoSite

@admin.register(Tarent)
class Tarent(admin.ModelAdmin):
   pass

@admin.register(TarentPersonality)
class TarentPersonality(admin.ModelAdmin):
   pass

@admin.register(TarentFace)
class TarentFace(admin.ModelAdmin):
   pass

@admin.register(TarentBody)
class TarentBody(admin.ModelAdmin):
   pass

@admin.register(TarentUpperBody)
class TarentUpperBody(admin.ModelAdmin):
   pass

@admin.register(TarentLowerBody)
class TarentLowerBody(admin.ModelAdmin):
   pass

@admin.register(TarentBraSize)
class TarentBraSize(admin.ModelAdmin):
   pass
@admin.register(TarentArtInfoSiteArticle)
class TarentArtInfoSiteArticle(admin.ModelAdmin):
   pass
@admin.register(TarentArt)
class TarentArt(admin.ModelAdmin):
   pass

@admin.register(AffiliateProvider)
class AffiliateProvider(admin.ModelAdmin):
   pass
@admin.register(TarentArtSampleImage)
class TarentArtSampleImage(admin.ModelAdmin):
   pass

@admin.register(TarentArtFetishism)
class TarentArtFetishism(admin.ModelAdmin):
   pass

@admin.register(TarentTimeline)
class TarentTimeline(admin.ModelAdmin):
   pass

@admin.register(TarentSite)
class TarentSite(admin.ModelAdmin):
   pass

@admin.register(SiteType)
class SiteType(admin.ModelAdmin):
   pass

@admin.register(InfoSite)
class InfoSite(admin.ModelAdmin):
   pass