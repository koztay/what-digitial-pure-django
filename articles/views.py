from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DeleteView, DetailView, FormView, ListView, TemplateView, UpdateView, View

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


class ArticleDetailView(DetailView):
    model = Article

    def get_object(self):
        return get_object_or_404(Article, pk=self.kwargs["pk"])
