from django.db import models
from django.utils import timezone

# Create your models here.

class TarentPersonality(models.Model):
    name = models.CharField(
        verbose_name = "性格",
        max_length = 40,
    )
    def __str__(self):
        return f'{self.name}'

class TarentFace(models.Model):
    name = models.CharField(
        verbose_name = "顔の傾向",
        max_length = 40,
    )
    memo = models.TextField(
        verbose_name = "顔についてメモ",
        max_length = 200,
        blank=True,
        null=True,
    )
    def __str__(self):
        return f'{self.name}'

class TarentBody(models.Model):
    name = models.CharField(
        verbose_name = "ボディ",
        max_length = 40,
    )
    def __str__(self):
        return f'{self.name}'

class TarentUpperBody(models.Model):
    name = models.CharField(
        verbose_name = "上半身",
        max_length = 40,
    )
    def __str__(self):
        return f'{self.name}'

class TarentLowerBody(models.Model):
    name = models.CharField(
        verbose_name = "下半身",
        max_length = 40,
    )
    def __str__(self):
        return f'{self.name}'

class TarentBraSize(models.Model):
    name = models.CharField(
        verbose_name = "ブラのサイズ",
        max_length = 2,
    )
    memo = models.TextField(
        verbose_name = "サイズについてメモ",
        max_length = 200,
        blank=True,
        null=True,
    )
    def __str__(self):
        return f'{self.name}'

class Tarent(models.Model):

    stage_name = models.CharField(
        verbose_name = "芸名。無いなら、芸能ニュースなどでの呼称",
        max_length = 40,
    )
    family_name = models.CharField(
        verbose_name = "性(漢字)漢字が無い外国人ならカタカナ",
        max_length = 40,
    )
    first_name = models.CharField(
        verbose_name = "名(漢字)漢字が無い外国人ならカタカナ",
        max_length = 40,
        blank=True,
        null=True,
    )
    family_katakana_name = models.CharField(
        verbose_name = "セイ(カナ)",
        max_length = 40,
        blank=True,
        null=True,
    )
    first_katakana_name = models.CharField(
        verbose_name = "メイ(カナ)",
        max_length = 40,
        blank=True,
        null=True,
    )
    family_rome_name = models.CharField(
        verbose_name = "性(ローマ字)",
        max_length = 40,
    )
    first_rome_name = models.CharField(
        verbose_name = "名(ローマ字)",
        max_length = 40,
    )
    image = models.URLField(
        verbose_name = "画像へのurl",
        max_length = 80,
        blank=True,
        null=True,
    )
    review = models.TextField(
        verbose_name = "レビュー",
        max_length = 800,
        blank=True,
        null=True,
    )
    birth_date = models.DateField(
        verbose_name = "誕生日(分からなければ空欄)",
        blank=True,
        null=True,
    )
    charm_point = models.CharField(
        verbose_name = "良い点👍",
        max_length = 40,
        blank=True,
        null=True,
    )
    tarent_personality = models.ManyToManyField(
        TarentPersonality,
        verbose_name = "性格(こっちから見えるでよい。)",
    )
    tarent_face = models.ManyToManyField(
        TarentFace,
        verbose_name = "顔の傾向",
    )
    tarent_body = models.ManyToManyField(
        TarentBody,
        verbose_name = "ボディ",
    )
    tarent_upper_body = models.ManyToManyField(
        TarentUpperBody,
        verbose_name = "上半身",
    )
    tarent_lower_body = models.ManyToManyField(
        TarentLowerBody,
        verbose_name = "下半身",
    )
    tarent_bra_size = models.ForeignKey(
        TarentBraSize,
        verbose_name = "ブラのサイズ",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    def __str__(self):
        return f'{self.stage_name}'

class TarentArtFetishism(models.Model):
    name = models.CharField(
        verbose_name = "フェチ名",
        max_length = 40,
    )
    def __str__(self):
        return f'{self.name}'

class InfoSite(models.Model):
    name = models.CharField(
        verbose_name = "名前",
        max_length = 40,
    )
    url = models.URLField(
        verbose_name = "url",
        max_length = 40,
    )
    individual = models.BooleanField(
        verbose_name = "個人サイト",
        max_length = 40,
        default=True,
    )
    def __str__(self):
        return f'{self.name}'

class TarentArt(models.Model):
    name = models.CharField(
        verbose_name = "作品名",
        max_length = 40,
    )
    tarent = models.ForeignKey(
        Tarent,
        verbose_name='タレント',
        on_delete=models.PROTECT
    )
    title_img = models.CharField(
        verbose_name = "タイトル画像",
        max_length = 40,
        blank=True,
        null=True,
    )
    good_point = models.CharField(
        verbose_name = "良い点👍",
        max_length = 40,
        blank=True,
        null=True,
    )
    bad_point = models.CharField(
        verbose_name = "悪い点👎",
        max_length = 40,
        blank=True,
        null=True,
    )
    tarent_art_fetishism = models.ManyToManyField(
        TarentArtFetishism,
        verbose_name = "フェチ名",
    )
    published_date = models.DateField(
        verbose_name = "出版日",
    )
    def __str__(self):
        return f'{self.name}'

class TarentArtInfoSiteArticle(models.Model):
    url = models.URLField(
        verbose_name = "url",
        max_length = 40,
    )
    info_site = models.ForeignKey(
        InfoSite,
        verbose_name = "情報サイト名",
        on_delete=models.PROTECT,
    )
    tarent_art = models.ForeignKey(
        TarentArt,
        verbose_name = "紹介作品",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    def __str__(self):
        return f'{self.info_site}'

class AffiliateProvider(models.Model):
    name = models.CharField(
        verbose_name = "名前",
        max_length = 40,
    )
    url = models.URLField(
        verbose_name = "url",
        max_length = 40,
    )
    def __str__(self):
        return f'{self.name}'

class TarentArtSampleImage(models.Model):
    url = models.URLField(
        verbose_name = "サンプル画像url",
        max_length = 40,
    )
    html = models.CharField(
        verbose_name = "サンプル画像html",
        max_length = 40,
    )
    tarent_art = models.ForeignKey(
        TarentArt,
        verbose_name = "作品名",
        on_delete=models.PROTECT,
    )
    affiliate_provider = models.ForeignKey(
        AffiliateProvider,
        verbose_name = "サンプル画像提供元",
        on_delete=models.PROTECT,
    )
    sort = models.IntegerField(
        verbose_name = '表示順',
        default = 0
    )

    def __str__(self):
        return f'{self.name}'

class SiteType(models.Model):
    name = models.CharField(
        verbose_name = "サイトタイプ",
        max_length = 40,
    )
    def __str__(self):
        return f'{self.name}'

class TarentTimeline(models.Model):

    tarent = models.ForeignKey(
        Tarent,
        verbose_name='タレント',
        on_delete=models.PROTECT,
    )
    url = models.URLField(
        verbose_name = "timelineへのurl",
        max_length = 40,
        blank=True,
        null=True,
    )
    html = models.TextField(
        verbose_name = '埋め込みhtml',
        max_length = 200,
        blank=True,
        null=True,
        
    )
    site_type = models.ForeignKey(
        SiteType,
        verbose_name='サイトのタイプ',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return f'{self.tarent}タイムライン'

class TarentInfoSiteEmbed(models.Model):
    tarent = models.ForeignKey(
        Tarent,
        verbose_name='タレント',
        on_delete=models.PROTECT,
    )
    url = models.URLField(
        verbose_name = "埋め込み先のurl",
        max_length = 60,
        blank=True,
        null=True,
    )

    html = models.TextField(
        verbose_name = "embed_html",
        max_length = 8000,
    )
    
    site_type = models.ForeignKey(
        SiteType,
        verbose_name='サイトのタイプ',
        on_delete=models.PROTECT
    )
    sort = models.IntegerField(
        verbose_name = '表示順',
        default = 0
    )
    def __str__(self):
        return f'{self.site_type}'


class TarentSite(models.Model):

    url = models.URLField(
        verbose_name = "url",
    )
    site_type = models.ForeignKey(
        SiteType,
        verbose_name='サイトのタイプ',
        on_delete=models.PROTECT
    )
    tarent = models.ForeignKey(
        Tarent,
        verbose_name='タレント',
        on_delete=models.PROTECT
    )
    def __str__(self):
        return f'{self.tarent}のサイト'


