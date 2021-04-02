# Generated by Django 3.1.7 on 2021-04-02 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Urun ismi')),
                ('content', models.TextField(max_length=500, verbose_name='Urun Aciklamasi')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('stock_count', models.PositiveSmallIntegerField(verbose_name='stok_adeti')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Urun Fiyati')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'db_table': 'urunler',
            },
        ),
    ]