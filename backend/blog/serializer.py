from rest_framework import serializers
from .models import Tarent,TarentPersonality,TarentFace,TarentBody,TarentUpperBody,TarentLowerBody,TarentBraSize,TarentArt,TarentArtFetishism,TarentTimeline,TarentSite,SiteType

class TarentSerializer(serializers.ModelSerializer):
   class Meta:
       model = Tarent
       fields = ('id', 'draft', 'published_at')

class TarentPersonalitySerializer(serializers.ModelSerializer):
   class Meta:
       model = TarentPersonality
       fields = ('id', 'draft', 'published_at')

class TarentFaceSerializer(serializers.ModelSerializer):
   class Meta:
       model = TarentFace
       fields = ('id', 'draft', 'published_at')

class TarentBodySerializer(serializers.ModelSerializer):
   class Meta:
       model = TarentBody
       fields = ('id', 'draft', 'published_at')

class TarentUpperBodySerializer(serializers.ModelSerializer):
   class Meta:
       model = TarentUpperBody
       fields = ('id', 'draft', 'published_at')

class TarentLowerBodySerializer(serializers.ModelSerializer):
   class Meta:
       model = TarentLowerBody
       fields = ('id', 'draft', 'published_at')

class TarentBraSizeSerializer(serializers.ModelSerializer):
   class Meta:
       model = TarentBraSize
       fields = ('id', 'draft', 'published_at')

class TarentArtSerializer(serializers.ModelSerializer):
   class Meta:
       model = TarentArt
       fields = ('id', 'draft', 'published_at')

class TarentArtFetishismSerializer(serializers.ModelSerializer):
   class Meta:
       model = TarentArtFetishism
       fields = ('id', 'draft', 'published_at')

class TarentTimelineSerializer(serializers.ModelSerializer):
   class Meta:
       model = TarentTimeline
       fields = ('id', 'draft', 'published_at')

class TarentSiteSerializer(serializers.ModelSerializer):
   class Meta:
       model = TarentSite
       fields = ('id', 'draft', 'published_at')

class SiteTypeSerializer(serializers.ModelSerializer):
   class Meta:
       model = SiteType
       fields = ('id', 'draft', 'published_at')