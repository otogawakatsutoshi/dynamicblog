# Generated by Django 3.1 on 2020-08-28 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_tarentinfositeembed_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarentbrasize',
            name='memo',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='サイズについてメモ'),
        ),
    ]
