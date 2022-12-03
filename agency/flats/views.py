from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView, FormView
from django.http import HttpResponseRedirect

from .forms import *


def catalog_ap(request):
    """Каталог квартир"""
    active = ['service']

    flats_list = Flat.objects.all()
    paginator = Paginator(flats_list, 6)

    page = request.GET.get('page')
    try:
        flats = paginator.page(page)
    except PageNotAnInteger:
        flats = paginator.page(1)
    except EmptyPage:
        flats = paginator.page(paginator.num_pages)
    page_range = paginator.page_range
    return render(request, 'flats/catalog-ap.html', {"flats": flats,
                                                     "page_range": page_range,
                                                     "active": active})


class FlatDetailView(FormView, DetailView):
    """Отображение страницы с квартирой"""
    active = ['service']
    model = Flat
    form_class = BuyOrderForm
    template_name = 'flats/ap-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flats'] = Flat.objects.all()
        context['gallery'] = FlatGallery.objects.filter(flat=context['flat'])
        print(context)
        return context

    def post(self, request, slug, *args, **kwargs):
        form = BuyOrderForm(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            new_form = form.save(commit=False)
            new_form.flat = Flat.objects.get(slug=slug)
            new_form.save()
        return HttpResponseRedirect(self.request.path_info)
