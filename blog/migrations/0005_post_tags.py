# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags', to='taggit.Tag'),
            preserve_default=True,
        ),
    ]
