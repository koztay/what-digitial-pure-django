from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DeleteView, DetailView, FormView, ListView, TemplateView, UpdateView, View

from taggit.models import Tag

from .models import Article


class HomePageView(TemplateView):
    template_name = 'articles/home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context["homepage_articles"] = Article.objects.all().order_by(
            "-pk")[:5]  # latest 5 article
        return context


class ArticleListView(ListView):
    model = Article
    paginate_by = 5


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self):
        return get_object_or_404(Article, pk=self.kwargs["pk"])


class ArticleListTagFilterView(ListView):
    model = Article
    paginate_by = 5
    
    def get_queryset(self, *args, **kwargs):
        qs = super(ArticleListTagFilterView, self).get_queryset()
        tag_slug = self.kwargs["tag_slug"]
        tag_id = self.kwargs["tag_id"]
        tag = get_object_or_404(Tag, slug=tag_slug, id=tag_id)
        qs = qs.filter(tags__in=[tag])
        return qs
