# -*- coding: utf-8 -*-
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ThumbnailMeta',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                             related_name='thumbnails', to='thumbnails.Source')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='thumbnailmeta',
            unique_together={('source', 'size')},
        ),
    ]
