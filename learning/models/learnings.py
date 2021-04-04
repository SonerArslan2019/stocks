from django.db import models
from django.contrib.auth.models import User



class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Urun ismi")
    content = models.TextField(verbose_name="Urun Aciklamasi", max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(verbose_name='Aktif', default=True)
    stock_count = models.PositiveSmallIntegerField(verbose_name="stok_adeti")
    price = models.DecimalField(verbose_name="Urun Fiyati", decimal_places=2, max_digits=10)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, verbose_name='Sahip', on_delete=models.CASCADE)


    class Meta:
        db_table = "urunler"
        verbose_name = 'Urun'
        verbose_name_plural = 'Urunler'

    def __str__(self):
        return self.name
