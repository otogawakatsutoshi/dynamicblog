from rest_framework import serializers
from . import models

class TarentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tarent
        fields = (
            'id',
            'stage_name',
            'family_name',
            'first_name',
            'family_katakana_name',
            'first_katakana_name',
            'family_rome_name',
            'first_rome_name',
            'charm_point',
            'birth_date',
            'tarent_personality',
            'tarent_face',
            'tarent_body',
            'tarent_upper_body',
            'tarent_lower_body',
            'tarent_bra_size',
        )

class TarentPersonalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TarentPersonality
        fields = ('id', 'draft', 'published_at')

class TarentFaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TarentFace
        fields = ('id', 'draft', 'published_at')

class TarentBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TarentBody
        fields = ('id', 'draft', 'published_at')

class TarentUpperBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TarentUpperBody
        fields = ('id', 'draft', 'published_at')

class TarentLowerBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TarentLowerBody
        fields = ('id', 'draft', 'published_at')

class TarentBraSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TarentBraSize
        fields = ('id', 'draft', 'published_at')

class AffiliateProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AffiliateProvider
        fields = ('id', 'draft', 'published_at')

class TarentArtInfoSiteArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TarentArtInfoSiteArticle
        fields = ('id', 'draft', 'published_at')

class TarentArtSampleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TarentArtSampleImage
        fields = ('id', 'draft', 'published_at')

class InfoSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InfoSite
        fields = ('id', 'draft', 'published_at')

class TarentArtSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TarentArt
        fields = ('id', 'name')

class TarentArtFetishismSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TarentArtFetishism
        fields = ('id', 'draft', 'published_at')

class TarentTimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TarentTimeline
        fields = ('id', 'draft', 'published_at')

class TarentSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TarentSite
        fields = ('id', 'draft', 'published_at')

class SiteTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SiteType
        fields = ('id', 'draft', 'published_at')