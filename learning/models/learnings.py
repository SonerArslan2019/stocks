from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import itertools


class ProductManager(models.Manager):  # kendi urun yoneticimizide olusturabiliriz
    def active_products(self):
        return self.filter(active=1)


class Product(models.Model):
    items = ProductManager()  # default degil bu product manager calisacaktir.
    objects = models.Manager()  # birden fazla urun yonetiside olabilir..

    name = models.CharField(max_length=100, verbose_name="Urun ismi")
    content = models.TextField(verbose_name="Urun Aciklamasi", max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(verbose_name='Aktif', default=True)
    stock_count = models.PositiveSmallIntegerField(verbose_name="stok_adeti")
    price = models.DecimalField(verbose_name="Urun Fiyati", decimal_places=2, max_digits=10)
    slug = models.SlugField(unique=True, editable=False)
    author = models.ForeignKey(User, verbose_name='Sahip', on_delete=models.SET_NULL, null=True, related_name='products', related_query_name='product')
                # on_delete=models.CASCADE yerine on_delete=models.SET_NUL ve null=True yaparsak data yi inaktif eder ama database den silmez

    class Meta:
        # db_table = "urunler"
        verbose_name = 'Urun'
        verbose_name_plural = 'Urunler'

    def __str__(self):
        return self.name  # ADMIN panelinde kayitlari isme gore gosterir.

    def get_absolute_url(self):
        return '/learning/product/detail/%i/' % self.id  # ADMIN panelinden sitedeki urune link verir.

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id:
            self.slug = slugify(self.name)

            for slug_id in itertools.count(1):
                if not Product.objects.filter(slug=self.slug).exists():
                    break
                self.slug = '%s-%d' % (self.slug, slug_id)

        super(Product, self).save()

    @property
    def summary(self):
        return self.content[:50]  # content in kac karekter ile SINIRLANDIRILACAGINI belirtiriz..


class Category(models.Model):
    name = models.CharField(max_length=50)
    product = models.ManyToManyField(Product, related_name='categories', related_query_name='category')