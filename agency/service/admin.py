from django.contrib import admin
from .models import *


class ApartmentInline(admin.TabularInline):
    model = Apartment


class ComplexGalleryInline(admin.TabularInline):
    model = ComplexGallery


class HouseGalleryInline(admin.TabularInline):
    model = House


class ComplexAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [
        ComplexGalleryInline,
        HouseGalleryInline,
    ]


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('complex',)


class HouseAdmin(admin.ModelAdmin):
    inlines = [
        ApartmentInline,
    ]


class SaleOrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date')


admin.site.register(Complex, ComplexAdmin)
admin.site.register(House, HouseAdmin)
admin.site.register(SaleOrder, SaleOrderAdmin)

