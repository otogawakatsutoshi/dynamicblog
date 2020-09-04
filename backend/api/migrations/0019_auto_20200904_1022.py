# Generated by Django 3.1 on 2020-09-04 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20200904_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='javpop',
            name='download_link',
            field=models.BinaryField(blank=True, null=True, verbose_name='動画'),
        ),
        migrations.AlterField(
            model_name='javpoplink',
            name='download_link',
            field=models.CharField(max_length=60, verbose_name='ダウンロードへのリンク'),
        ),
        migrations.AlterField(
            model_name='javpoplink',
            name='javpop',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.javpop', unique=True, verbose_name='作品名'),
        ),
        migrations.CreateModel(
            name='JavPopVideoImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('画像', models.BinaryField(max_length=60, verbose_name='画像')),
                ('javpop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='api.javpop', unique=True, verbose_name='作品名')),
            ],
        ),
    ]
