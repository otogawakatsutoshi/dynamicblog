from django.contrib import admin
from django import forms
from . import models
from django.db import models as django_db_models
from guardian.admin import GuardedModelAdmin

class BinaryFileInput(forms.ClearableFileInput):

    def is_initial(self, value):
        """
        Return whether value is considered to be initial value.
        """
        return bool(value)

    def format_value(self, value):
        """Format the size of the value in the db.

        We can't render it's name or url, but we'd like to give some information
        as to wether this file is not empty/corrupt.
        """
        if self.is_initial(value):
            return f'{len(value)} bytes'


    def value_from_datadict(self, data, files, name):
        """Return the file contents so they can be put in the db."""
        upload = super().value_from_datadict(data, files, name)
        if upload:
            return upload.read()

@admin.register(models.JavPop)
class JavPop(GuardedModelAdmin):
    search_fields = ['name']
    formfield_overrides = {
        django_db_models.BinaryField: {'widget': BinaryFileInput()},
    }

@admin.register(models.JavPopLink)
class JavPopLink(GuardedModelAdmin):
    search_fields = ['javpop__name']
    def javpop_name(self, obj):
        return obj.javpop.name
    javpop_name.short_description = 'javpop_name'
    javpop_name.admin_order_field = 'javpop__name'

@admin.register(models.JavPopVideoImage)
class JavPopVideoImage(GuardedModelAdmin):
    search_fields = ['javpop__name']
    formfield_overrides = {
        django_db_models.BinaryField: {'widget': BinaryFileInput()},
    }
    def javpop_name(self, obj):
        return obj.javpop.name
    javpop_name.short_description = 'javpop_name'
    javpop_name.admin_order_field = 'javpop__name'

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

@admin.register(models.TarentInfoSiteEmbed)
class TarentInfoSiteEmbed(GuardedModelAdmin):
    search_fields = ['tarent__stage_name']
    list_display = ('stage_name','site_type','sort')
    def stage_name(self, obj):
        return obj.tarent.stage_name
    stage_name.short_description = 'stage_name'
    stage_name.admin_order_field = 'tarent__stage_name'

    def site_type(self, obj):
        return obj.site_type.name
    site_type.short_description = 'site_type'
    site_type.admin_order_field = 'site_type__name'
