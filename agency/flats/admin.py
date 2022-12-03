from django.contrib import admin
from .models import *


class BuyOrderAdmin(admin.ModelAdmin):
    list_display = ('flat', 'name', 'phone')


class FlatGalleryInline(admin.TabularInline):
    model = FlatGallery


class FlatAdmin(admin.ModelAdmin):
    list_display = ('street', 'house_number', 'flat_number')
    inlines = [
        FlatGalleryInline,
    ]


class FlatGalleryAdmin(admin.ModelAdmin):
    list_display = ('flat',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(BuyOrder, BuyOrderAdmin)

