from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from ckeditor.fields import RichTextField
from parler.models import TranslatableModel, TranslatedFields
from sorl.thumbnail import ImageField
from taggit.managers import TaggableManager


class Article(TranslatableModel):

    image = ImageField(upload_to="article-images")
    tags = TaggableManager(blank=True)
    translations = TranslatedFields(
        title=models.CharField(
            max_length=128, verbose_name=_('article title')),
        slug=models.SlugField(_("article slug"), max_length=255, blank=True),
        content=RichTextField(verbose_name=_('article content')),
        any_language=True,
    )
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})
