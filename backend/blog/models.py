from django.db import models
from django.utils import timezone

# Create your models here.

class Tarent(models.Model):

    stage_name = models.CharField(
        verbose_name = "芸名。無いなら、芸能ニュースなどでの呼称",
        max_length = 40,
    )
    family_name = models.CharField(
        verbose_name = "性(漢字)漢字が無い外国人ならカタカナ",
        max_length = 40,
    )
    first_rome_name = models.CharField(
        verbose_name = "名(漢字)漢字が無い外国人ならカタカナ",
        max_length = 40,
    )
    family_rome_name = models.CharField(
        verbose_name = "性(ローマ字)",
        max_length = 40,
    )
    first_rome_name = models.CharField(
        verbose_name = "名(ローマ字)",
        max_length = 40,
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

    def __str__(self):
        return f'{self.stage_name}'

class TarentPersonality(models.Model):
    name = models.CharField(
        verbose_name = "性格(こっちから見えるでよい。)",
        max_length = 40,
    )
    def __str__(self):
        return f'{self.name}'

class TarentFace(models.Model):
    name = models.CharField(
        verbose_name = "顔の傾向",
        max_length = 40,
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
    published_date = models.DateField(
        verbose_name = "出版日",
    )
    
    def __str__(self):
        return f'{self.name}'

class TarentArtFetishism(models.Model):
    name = models.CharField(
        verbose_name = "作品名",
        max_length = 40,
    )
    tarent = models.ForeignKey(
        Tarent,
        verbose_name='タレント',
        on_delete=models.PROTECT
    )
    published_date = models.DateField(
        verbose_name = "出版日",
    )
    
    def __str__(self):
        return f'{self.name}'

class TarentTimeline(models.Model):
    isbn = models.CharField(
        verbose_name = "ISBNコード",
        max_length = 40,
    )
    title = models.CharField(
        verbose_name = '署名',
        max_length = 40,
    )
    price = models.IntegerField(
        verbose_name = '価格',
    )
    publisher = models.CharField(
        verbose_name = "出版社",
        choices = [
            ('集英社','集英社'),
        ],
        max_length = 40,
    )
    draft = models.BooleanField(
        verbose_name = '下書き(チェックを外すと公開されます。)',
        default=True,
    )
    published_at = models.DateTimeField(
        verbose_name = "公開日時",
        default=timezone.now,
    )
    tarent = models.ForeignKey(
        Tarent,
        verbose_name='タレント',
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f'{self.tarent}タイムライン'

class SiteType(models.Model):
    name = models.CharField(
        verbose_name = "サイトタイプ",
        max_length = 40,
    )
    def __str__(self):
        return f'{self.name}'

class TarentSite(models.Model):

    url = models.URLField(
        verbose_name = "url",
    )
    site_type = models.ForeignKey(
        SiteType,
        verbose_name='タレント',
        on_delete=models.PROTECT
    )
    tarent = models.ForeignKey(
        Tarent,
        verbose_name='タレント',
        on_delete=models.PROTECT
    )
    def __str__(self):
        return f'{self.tarent}SNS'


