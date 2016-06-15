# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160613_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=django_markdown.models.MarkdownField(verbose_name='content'),
        ),
    ]
