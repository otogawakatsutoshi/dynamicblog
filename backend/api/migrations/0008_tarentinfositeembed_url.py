# Generated by Django 3.1 on 2020-08-28 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200828_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarentinfositeembed',
            name='url',
            field=models.URLField(blank=True, max_length=60, null=True, verbose_name='埋め込み先のurl'),
        ),
    ]
