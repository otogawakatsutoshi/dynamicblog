# Generated by Django 3.1 on 2020-08-30 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20200829_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarent',
            name='review',
            field=models.TextField(blank=True, max_length=800, null=True, verbose_name='レビュー'),
        ),
    ]
