# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_item_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
    ]
