# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls

from articles.views import HomePageView


urlpatterns = [
    # add your own patterns here
] + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    url(r'^$', HomePageView.as_view(), name='home'),
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)
