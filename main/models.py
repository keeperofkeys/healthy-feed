# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class NewsItem(models.Model):
    class META:
        ordering = '-date'

    title = models.TextField(blank=False)
    url = models.CharField(blank=False, max_length=1024, unique=True)
    date = models.DateTimeField(null=True)
    author = models.CharField(blank=True, max_length=255)
    source = models.CharField(blank=True, max_length=100)

    def __string__(self):
        return self.title

