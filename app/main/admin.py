from django.contrib import admin

from .models import Apartment, Images

# Register your models here.


class ApartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "city", "street", "house_number", "is_published")
    list_display_links = ("id",)
    search_fields = ("Apartment",)
    prepopulated_fields = {"slug": ("city", "street", "house_number")}


class ImagesAdmin(admin.ModelAdmin):
    list_display = ("id", "apartment")


admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(Images, ImagesAdmin)
