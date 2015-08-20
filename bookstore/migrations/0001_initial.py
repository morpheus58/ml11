# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('publisher', models.CharField(max_length=50)),
                ('summary', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('purchase_link', models.URLField()),
                ('cover_img', models.URLField()),
                ('author', models.ManyToManyField(to='bookstore.Authors')),
            ],
        ),
    ]
