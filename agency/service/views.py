from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView, FormView

from .forms import *


def service(request):
    """Раздел 'Услуги' """
    active = ['service']
    return render(request, 'service/service.html', locals())


def catalog_nb(request):
    """Каталог новостроек"""
    active = ['service']
    complex_list = Complex.objects.all()
    paginator = Paginator(complex_list, 3)

    page = request.GET.get('page')
    try:
        complexes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        complexes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        complexes = paginator.page(paginator.num_pages)
    page_range = paginator.page_range
    return render(request, 'service/catalog-nb.html', {"complexes": complexes,
                                                       "page_range": page_range,
                                                       "active": active})


class ComplexDetailView(DetailView):
    """Отображение комплекса"""
    active = ['service']
    model = Complex
    template_name = 'service/complex.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery'] = ComplexGallery.objects.filter(complex=context['complex'])
        context['houses'] = House.objects.filter(complex=context['complex'])
        context['apartments'] = {h.pk: Apartment.objects.filter(house=h) for h in context['houses']}
        for h in context['houses']:
            print(h.id)

        return context


class Sell(FormView):
    """Продажа квартиры"""
    active = ['service']
    model = SaleOrder
    form_class = SaleOrderForm
    template_name = 'service/sell-ap.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sale_order_form'] = SaleOrder()
        return context

    def post(self, request, *args, **kwargs):
        form = SaleOrderForm(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            new_form = form.save(commit=False)
            new_form.save()
        return HttpResponseRedirect(self.request.path_info)

