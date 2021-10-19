# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf.urls.i18n import set_language
from django.utils.translation import ugettext_lazy as _

from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls


from articles.views import HomePageView, ArticleListView, ArticleDetailView


urlpatterns = [
    # add your own patterns here
] + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    url(r'^$', HomePageView.as_view(), name='home'),
    url(_(r'^articles/$'), ArticleListView.as_view(), name='article_list'),
    url(_(r'^articles/(?P<slug>[-\w]+)/(?P<pk>\d+)/$'),
        ArticleDetailView.as_view(), name='article_detail'),
    url('^i18n/setlang/', set_language, name='set_language'),
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)
