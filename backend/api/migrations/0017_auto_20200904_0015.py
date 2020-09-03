# Generated by Django 3.1 on 2020-09-03 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20200904_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarent',
            name='family_katakana_name',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='セイ(カナ)'),
        ),
        migrations.AlterField(
            model_name='tarent',
            name='family_name',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='性(漢字)漢字が無い外国人ならカタカナ'),
        ),
        migrations.AlterField(
            model_name='tarent',
            name='family_rome_name',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='性(ローマ字)'),
        ),
        migrations.AlterField(
            model_name='tarent',
            name='first_katakana_name',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='メイ(カナ)'),
        ),
        migrations.AlterField(
            model_name='tarent',
            name='first_name',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='名(漢字)漢字が無い外国人ならカタカナ'),
        ),
        migrations.AlterField(
            model_name='tarent',
            name='first_rome_name',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='名(ローマ字)'),
        ),
        migrations.AlterField(
            model_name='tarent',
            name='image',
            field=models.URLField(blank=True, max_length=80, null=True, unique=True, verbose_name='画像へのurl'),
        ),
    ]
