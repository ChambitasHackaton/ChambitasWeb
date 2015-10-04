# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True)),
                ('price', models.FloatField(default=0.0)),
                ('id_employees', models.ForeignKey(related_name='empleados', to=settings.AUTH_USER_MODEL)),
                ('id_employers', models.ForeignKey(related_name='empleadores', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
