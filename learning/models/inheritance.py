from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(verbose_name='isim', max_length=100)
    content = models.TextField(verbose_name='aciklama')
    author = models.ForeignKey(User, verbose_name='sahip', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True  # Database de Abstract True oldugu icin gozukmez, ama etkindir.


class BookCompany(Company):
    pass


class GameCompany(Company):
    pass


class Book(models.Model):
    name = models.CharField(max_length=100)
    page_count = models.PositiveSmallIntegerField()


class Intro(Book):
    content = models.TextField()


class ProxyBookManager(models.Manager):  # vekil sinifina model yoneticisi eklenebilir.
    pass


class ProxyBook(Book):  # Database de vekil bir model ornegi, kendisi yok

    objects = ProxyBookManager()  # vekil sinifin yoneticisi, yazilan metodlarda kullanilir.

    class Meta:
        proxy = True
        ordering = ['name']

    @property
    def short_name(self):
        return self.name[:10]
