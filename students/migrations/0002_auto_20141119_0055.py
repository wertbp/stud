# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442', 'verbose_name_plural': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u0438'},
        ),
        migrations.AddField(
            model_name='student',
            name='photo',
            field=models.ImageField(upload_to=b'', null=True, verbose_name='\u0424\u043e\u0442\u043e', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043d\u0430\u0440\u043e\u0434\u0436\u0435\u043d\u043d\u044f'),
            preserve_default=True,
        ),
    ]
