# Generated by Django 3.1 on 2020-09-04 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20200904_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='javpopvideoimage',
            name='画像',
        ),
        migrations.AddField(
            model_name='javpopvideoimage',
            name='image',
            field=models.BinaryField(blank=True, editable=True, max_length=60, null=True, verbose_name='画像'),
        ),
    ]