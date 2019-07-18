"""feeds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from main.views import homepage, live_feed, kill_story, show_post, site_search

urlpatterns = [
    url(r'^$', homepage),
    url(r'^live/', live_feed),
    url(r'^search/', site_search, name='search'),
    url(r'^posts/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>.+)/', show_post),
    url(r'^kill-story/', kill_story),
    url(r'^about/', TemplateView.as_view(template_name="main/about.html"), name='about'),
    url(r'^admin/', admin.site.urls),
    url(r'^comments/', include('django_comments_xtd.urls')),
    url(r'^auth/', include('django.contrib.auth.urls')),
]
