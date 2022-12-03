from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import F

from .forms import *


class index(FormView):
    """Главная страница"""
    active = ['home']
    model = Feedback
    form_class = FeedbackForm
    template_name = 'mainApp/homePage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feedback_form'] = FeedbackForm()
        return context

    def post(self, request, *args, **kwargs):
        form = FeedbackForm(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            new_form = form.save(commit=False)
            new_form.save()
        return HttpResponseRedirect(self.request.path_info)


def news(request):
    """Раздел с новостями"""
    active = ['articles']

    article_list = Article.objects.all()
    paginator = Paginator(article_list, 2)

    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    page_range = paginator.page_range
    return render(request, 'mainApp/news.html', {"articles": articles,
                                                 "page_range": page_range,
                                                 "active": active})


def about(request):
    """Раздел 'О нас' """
    active = ['about']
    return render(request, 'mainApp/about.html', locals())


class contacts(FormView):
    """Раздел 'Контакты' """
    active = ['contacts']
    model = Feedback
    form_class = FeedbackForm
    template_name = 'mainApp/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feedback_form'] = FeedbackForm()
        return context

    def post(self, request, *args, **kwargs):
        form = FeedbackForm(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            new_form = form.save(commit=False)
            new_form.save()
        return HttpResponseRedirect(self.request.path_info)


class ArticleDetailView(FormView, DetailView):
    """Отдельная статья"""
    active = ['articles']
    model = Article
    form_class = FormComment
    template_name = 'mainApp/article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_list'] = Comment.objects.filter(article=context['article'])
        context['comment_form'] = FormComment()
        Article.objects.filter(title=context['article']).update(views=F("views") + 1)
        return context

    def post(self, request, slug, *args, **kwargs):
        form = FormComment(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            new_form = form.save(commit=False)
            new_form.article = Article.objects.get(slug=slug)
            new_form.save()
        return HttpResponseRedirect(self.request.path_info)


class ReviewsDetailView(FormView):
    """Отзывы"""
    active = ['reviews']
    model = Review
    form_class = ReviewForm
    template_name = 'mainApp/reviews.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews_list'] = Review.objects.all()
        context['review_form'] = ReviewForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            new_form = form.save(commit=False)
            new_form.save()
        return HttpResponseRedirect(self.request.path_info)
