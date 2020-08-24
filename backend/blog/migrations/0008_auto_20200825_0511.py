# Generated by Django 3.1 on 2020-08-24 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_tarentartinfositearticle_tarent_art'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarent',
            name='family_katakana_name',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='セイ(カナ)'),
        ),
        migrations.AddField(
            model_name='tarent',
            name='first_katakana_name',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='メイ(カナ)'),
        ),
        migrations.AddField(
            model_name='tarent',
            name='first_name',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='名(漢字)漢字が無い外国人ならカタカナ'),
        ),
    ]
