# Generated by Django 3.1 on 2020-09-04 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20200904_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='javpop',
            name='download_link',
            field=models.BinaryField(blank=True, editable=True, null=True, verbose_name='動画'),
        ),
        migrations.AlterField(
            model_name='javpoplink',
            name='javpop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.javpop', verbose_name='作品名'),
        ),
    ]