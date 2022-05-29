from django.shortcuts import render, get_object_or_404
from django.conf import settings

from .models import Apartment, Images

# Create your views here.


def index(request):
    apartments = Apartment.objects.all()
    context = {
        "apartments": apartments,
        "title": "Аренда апартаментов",
    }
    return render(request, "index.html", context)


def apartment(request, slug):
    apartment = get_object_or_404(Apartment, slug=slug)
    images = Images.objects.filter(apartment_id=apartment.id)
    context = {
        "apartment": apartment,
        "images": images,
        "title": apartment,
        "YMAPS_API_KEY": settings.YMAPS_API_KEY,
    }
    return render(request, "apartment.html", context)


def about(request):
    context = {
        "title": "Аренда апартаментов",
    }
    return render(request, "about.html", context)
