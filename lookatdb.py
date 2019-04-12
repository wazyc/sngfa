#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings
import django

settings.configure(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': './db.sqlite3',
        }
    },
    INSTALLED_APPS=['kadoumap.apps.KadoumapConfig']
)
django.setup()

from kadoumap.models import OpeData

for q in OpeData.objects.all():
    print(q.ope_datetime, q.ope_state, q.ope_machine)
