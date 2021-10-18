from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from parler.admin import TranslatableAdmin
# from sorl.thumbnail.admin import AdminImageMixin

from . import models
@admin.register(models.Article)
class ArticleAdmin(TranslatableAdmin):
    list_filter = ("tags",)
    fieldsets = (
        (1, {"fields": ("image", "tags", )}),
        (
            _("Translatable Fields"),
            {"fields": ("title", "slug", "content")},
        ),
    )

    def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {"slug": ("title",)}
