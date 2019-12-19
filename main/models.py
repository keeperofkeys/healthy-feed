# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class NewsItem(models.Model):
    class Meta:
        ordering = ('-date',)

    title = models.TextField(blank=False)
    url = models.CharField(blank=False, max_length=1024, unique=True)
    date = models.DateTimeField(null=True)
    author = models.CharField(blank=True, max_length=255)
    source = models.CharField(blank=True, max_length=100)
    summary = models.TextField(blank=True)
    slug = models.CharField(blank=True, max_length=100)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.title)
        super(NewsItem, self).save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('story-comments', kwargs={
            'year':self.date.year,
            'month':self.date.month,
            'day': self.date.day,
            'slug': self.slug})


