from django.db import connection
from rest_framework import filters, generics, viewsets,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from . import models,serializer

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

class TarentViewSet(APIView):
    def get(self, request, id,format=None):
#        queryset = models.Tarent.objects.get(pk=id)
#        json = serializer.TarentSerializer(queryset)
#        return Response(json.data)

#        tarent = models.Tarent.objects.get(pk=id)
       
        cursor = connection.cursor()
        cursor.execute(
"""
SELECT api_tarent.id,
    api_tarent.stage_name,
    api_tarent.family_name,
    api_tarent.first_name, 
    api_tarent.family_katakana_name,
    api_tarent.first_katakana_name,
    api_tarent.family_rome_name,
    api_tarent.first_rome_name,
    api_tarent.birth_date,     
    api_tarent.charm_point,
    group_concat(DISTINCT api_tarentpersonality.id) AS tarent_personality_id,
    group_concat(DISTINCT api_tarentpersonality.name) AS tarent_personality_name,
	group_concat(DISTINCT api_tarentface.id) AS tarent_face_id,
    group_concat(DISTINCT api_tarentface.name) AS tarent_face_name,
	group_concat(DISTINCT api_tarentbody.id) AS tarent_body_id,
    group_concat(DISTINCT api_tarentbody.name) AS tarent_body_name,
	group_concat(DISTINCT api_tarentlowerbody.id) AS tarent_lowerbody_id,
    group_concat(DISTINCT api_tarentlowerbody.name) AS tarent_lowerbody_name,
	group_concat(DISTINCT api_tarentupperbody.id) AS tarent_upperbody_id,
    group_concat(DISTINCT api_tarentupperbody.name) AS tarent_upperbody_name,
	api_tarentbrasize.id AS tarent_brasize_id,
    api_tarentbrasize.name AS tarent_brasize_name,
    group_concat(DISTINCT api_tarentart.id) AS tarent_art_id,
	group_concat(DISTINCT api_tarentart.name) AS tarent_art_name,
	group_concat(DISTINCT api_tarentsite.url) AS tarent_site_url,
	group_concat(DISTINCT api_sitetype.name) AS site_type_name,
    group_concat(DISTINCT CASE api_sitetype2.name
		WHEN 'twitter' then api_tarentinfositeembed.html
		ELSE NULL
	END) AS  twitter_embed_html,
	group_concat(DISTINCT CASE api_sitetype2.name
		WHEN 'twitter' then api_tarentinfositeembed.url
		ELSE NULL
	END) AS  twitter_embed_url,
	group_concat(DISTINCT CASE api_sitetype2.name
		WHEN 'instagram' then api_tarentinfositeembed.html
		ELSE NULL
	END) AS  instagram_embed_html,
	group_concat(DISTINCT CASE api_sitetype2.name
		WHEN 'instagram' then api_tarentinfositeembed.url
		ELSE NULL
	END) AS  instagram_embed_url,
	group_concat(DISTINCT CASE api_sitetype2.name
		WHEN 'youtube' then api_tarentinfositeembed.html
		ELSE NULL
	END) AS  youtube_embed_html,
	group_concat(DISTINCT CASE api_sitetype2.name
		WHEN 'youtube' then api_tarentinfositeembed.url
		ELSE NULL
	END) AS  youtube_embed_url

    FROM api_Tarent
    INNER JOIN api_tarent_tarent_personality
        ON api_Tarent.id = api_tarent_tarent_personality.tarent_id
    INNER JOIN api_tarentpersonality
        ON api_tarent_tarent_personality.tarentpersonality_id = api_tarentpersonality.id
	
	INNER JOIN api_tarent_tarent_face
        ON api_Tarent.id = api_tarent_tarent_face.tarent_id
    INNER JOIN api_tarentface
        ON api_tarent_tarent_face.tarentface_id = api_tarentface.id
		
	INNER JOIN api_tarent_tarent_body
        ON api_Tarent.id = api_tarent_tarent_body.tarent_id
    INNER JOIN api_tarentbody
        ON api_tarent_tarent_body.tarentbody_id = api_tarentbody.id
    
    INNER join api_tarent_tarent_lower_body
        ON api_Tarent.id= api_tarent_tarent_lower_body.tarent_id
	INNER JOIN api_tarentlowerbody
        ON api_tarent_tarent_lower_body.tarentlowerbody_id = api_tarentlowerbody.id
		
	INNER join api_tarent_tarent_upper_body
        ON api_Tarent.id= api_tarent_tarent_upper_body.tarent_id
	INNER JOIN api_tarentupperbody
        ON api_tarent_tarent_upper_body.tarentupperbody_id = api_tarentupperbody.id
	INNER JOIN api_tarentbrasize
		ON api_Tarent.tarent_bra_size_id = api_tarentbrasize.id
    INNER JOIN api_tarentart
		ON api_tarent.id = api_tarentart.tarent_id
    INNER JOIN api_tarentsite
		ON api_tarent.id = api_tarentsite.tarent_id
	INNER JOIN api_sitetype
		ON api_tarentsite.site_type_id = api_sitetype.id

    INNER JOIN api_tarentinfositeembed
		ON api_tarent.id = api_tarentinfositeembed.tarent_id
	INNER JOIN api_sitetype AS api_sitetype2
		ON api_tarentinfositeembed.site_type_id = api_sitetype2.id
		AND api_sitetype2.name IN ('instagram','youtube','twitter')

    WHERE api_Tarent.id = %s
    GROUP BY api_tarent.stage_name,
        api_tarent.family_name,
        api_tarent.first_name, 
        api_tarent.family_katakana_name,
        api_tarent.first_katakana_name,
        api_tarent.family_rome_name,
        api_tarent.first_rome_name,
        api_tarent.birth_date,     
        api_tarent.charm_point,
	    api_tarentbrasize.id,
	    api_tarentbrasize.name
""",
        [id])
        # 一行であることは確定なので[0]でjsonに戻す。
        queryset = dictfetchall(cursor)[0]


        queryset['tarent_personality_id'] = queryset['tarent_personality_id'].split(",")
        queryset['tarent_personality_name'] = queryset['tarent_personality_name'].split(",")
        queryset['tarent_face_id'] = queryset['tarent_face_id'].split(",")
        queryset['tarent_face_name'] = queryset['tarent_face_name'].split(",")
        queryset['tarent_body_id'] = queryset['tarent_body_id'].split(",")
        queryset['tarent_body_name'] = queryset['tarent_body_name'].split(",")
        queryset['tarent_lowerbody_id'] = queryset['tarent_lowerbody_id'].split(",")
        queryset['tarent_lowerbody_name'] = queryset['tarent_lowerbody_name'].split(",")
        queryset['tarent_upperbody_id'] = queryset['tarent_upperbody_id'].split(",")
        queryset['tarent_upperbody_name'] = queryset['tarent_upperbody_name'].split(",")
        queryset['tarent_art_id'] = queryset['tarent_art_id'].split(",")
        queryset['tarent_art_name'] = queryset['tarent_art_name'].split(",")
        queryset['tarent_site_url'] = queryset['tarent_site_url'].split(",")
        queryset['site_type_name'] = queryset['site_type_name'].split(",")
        if queryset['twitter_embed_html'] is not None:
            queryset['twitter_embed_html'] = queryset['twitter_embed_html'].split(",")
        if queryset['twitter_embed_url'] is not None:
            queryset['twitter_embed_url'] = queryset['twitter_embed_url'].split(",")
        if queryset['instagram_embed_html'] is not None:
            queryset['instagram_embed_html'] = queryset['instagram_embed_html'].split(",")
        if queryset['instagram_embed_url'] is not None:
            queryset['instagram_embed_url'] = queryset['instagram_embed_url'].split(",")
        if queryset['youtube_embed_html'] is not None:
            queryset['youtube_embed_html'] = queryset['youtube_embed_html'].split(",")
        if queryset['youtube_embed_url'] is not None:
            queryset['youtube_embed_url'] = queryset['youtube_embed_url'].split(",")

        return Response(queryset)

class TarentPersonalityViewSet(APIView):
    queryset = models.TarentPersonality.objects.all()
    serializer_class = serializer.TarentPersonalitySerializer
    #json = serializer.TarentSerializer(queryset, many=True)
    filter_fields = ('name',)

class TarentFaceViewSet(APIView):
    def get(self, request, id,format=None):
       
        cursor = connection.cursor()
        cursor.execute(
"""
SELECT api_tarentface.id,
		api_tarentface.name AS tarent_face_name,
        replace(replace(api_tarentface.memo,'\r\n','<br />'),'\n','<br />') AS tarent_face_memo,
		group_concat(api_tarent.id) AS tarent_id,
		group_concat(api_tarent.stage_name) AS tarent_stage_name
FROM api_tarentface
INNER JOIN api_tarent_tarent_face
	ON api_tarentface.id = api_tarent_tarent_face.tarentface_id
INNER JOIN api_tarent
	ON api_tarent_tarent_face.tarent_id = api_tarent.id
WHERE api_tarentface.id = %s
GROUP BY api_tarentface.id,
		api_tarentface.name
""",
        [id])
        # 一行であることは確定なので[0]でjsonに戻す。もしくはnullのときはエラー
        queryset = dictfetchall(cursor)[0]

        if queryset['tarent_id'] is not None:
            queryset['tarent_id'] = queryset['tarent_id'].split(",")
        if queryset['tarent_stage_name'] is not None:
            queryset['tarent_stage_name'] = queryset['tarent_stage_name'].split(",")
        
        return Response(queryset)


class TarentBodyViewSet(APIView):
    queryset = models.TarentBody.objects.all()
    serializer_class = serializer.TarentBodySerializer
    filter_fields = ('name',)

class TarentUpperBodyViewSet(APIView):
    queryset = models.TarentUpperBody.objects.all()
    serializer_class = serializer.TarentUpperBodySerializer
    filter_fields = ('name',)

class TarentLowerBodyViewSet(APIView):
    queryset = models.TarentLowerBody.objects.all()
    serializer_class = serializer.TarentLowerBodySerializer
    filter_fields = ('name',)

class TarentBraSizeViewSet(APIView):
   def get(self, request, id,format=None):
       
        cursor = connection.cursor()
        cursor.execute(
"""
SELECT api_tarentbrasize.id,
		api_tarentbrasize.name AS tarent_bra_size,
        replace(replace(api_tarentbrasize.memo,'\r\n','<br />'),'\n','<br />') AS tarent_bra_size_memo,
		group_concat(api_tarent.id) AS tarent_id,
		group_concat(api_tarent.stage_name) AS tarent_stage_name
FROM api_tarentbrasize
INNER JOIN api_tarent
	ON api_tarentbrasize.id = api_tarent.tarent_bra_size_id
WHERE api_tarentbrasize.id = %s
GROUP BY api_tarentbrasize.id,
        api_tarentbrasize.memo,
		api_tarentbrasize.name
""",
        [id])
        # 一行であることは確定なので[0]でjsonに戻す。もしくはnullのときはエラー
        queryset = dictfetchall(cursor)[0]

        if queryset['tarent_id'] is not None:
            queryset['tarent_id'] = queryset['tarent_id'].split(",")
        if queryset['tarent_stage_name'] is not None:
            queryset['tarent_stage_name'] = queryset['tarent_stage_name'].split(",")
        
        return Response(queryset)


class AffiliateProviderViewSet(APIView):
    queryset = models.AffiliateProvider.objects.all()
    serializer_class = serializer.AffiliateProviderSerializer
    filter_fields = ('name',)

class TarentArtInfoSiteArticleViewSet(APIView):
    queryset = models.TarentArtInfoSiteArticle.objects.all()
    serializer_class = serializer.TarentArtInfoSiteArticleSerializer
    filter_fields = ('name',)

class TarentArtSampleImageViewSet(APIView):
    queryset = models.TarentArtSampleImage.objects.all()
    serializer_class = serializer.TarentArtSampleImageSerializer
    filter_fields = ('name',)

class InfoSiteViewSet(APIView):
    queryset = models.InfoSite.objects.all()
    serializer_class = serializer.InfoSiteSerializer
    filter_fields = ('name',)

class TarentArtViewSet(APIView):
    queryset = models.TarentArt.objects.all()
    serializer_class = serializer.TarentArtSerializer
    filter_fields = ('name',)

class TarentArtFetishismViewSet(APIView):
    queryset = models.TarentArtFetishism.objects.all()
    serializer_class = serializer.TarentArtFetishismSerializer
    filter_fields = ('name',)

class TarentTimelineViewSet(APIView):
    queryset = models.TarentTimeline.objects.all()
    serializer_class = serializer.TarentTimelineSerializer
    filter_fields = ('draft',)

class TarentSiteViewSet(APIView):
    queryset = models.TarentSite.objects.all()
    serializer_class = serializer.TarentSiteSerializer
    filter_fields = ('name',)

class SiteTypeViewSet(APIView):
    queryset = models.SiteType.objects.all()
    serializer_class = serializer.SiteTypeSerializer
    filter_fields = ('name',)
