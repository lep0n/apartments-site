from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


def apartment_image_path(self, filename):
    return f"images/{self.slug}/main_img.jpg"


class Apartment(models.Model):
    country = models.CharField(max_length=30, default="Россия", verbose_name="Страна")
    city = models.CharField(max_length=30, verbose_name="Город")
    street = models.CharField(max_length=50, verbose_name="Улица")
    house_number = models.CharField(max_length=10, verbose_name="Номер дома")
    apartment_number = models.CharField(
        max_length=10, verbose_name="Номер апартаментов"
    )
    slug = models.SlugField(unique=True)
    main_image = models.ImageField(
        upload_to=apartment_image_path, verbose_name="Главное изображение"
    )
    description = models.TextField(verbose_name="Описание")
    phone = PhoneNumberField(null=False, blank=False, unique=False, verbose_name="Телефон")
    price = models.PositiveIntegerField(verbose_name="Цена за сутки")
    publish_date = models.DateField(auto_now_add=True, verbose_name="Дата публикации")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    def __str__(self):
        return ", ".join((self.city, self.street, self.house_number))

    class Meta:
        verbose_name = "Апартаменты"
        verbose_name_plural = "Апартаменты"
        ordering = ("slug",)


class Images(models.Model):
    apartment = models.ForeignKey(Apartment, default=None, on_delete=models.CASCADE)

    image = models.ImageField(upload_to="images/%Y/%m/%d")

    class Meta:
        verbose_name = "Фотографии"
        verbose_name_plural = "Фотографии"
