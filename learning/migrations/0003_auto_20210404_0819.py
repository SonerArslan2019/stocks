# Generated by Django 3.1.7 on 2021-04-04 05:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learning', '0002_auto_20210404_0611'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('items', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
        migrations.CreateModel(
            name='GameCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='isim')),
                ('content', models.TextField(verbose_name='aciklama')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='sahip')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BookCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='isim')),
                ('content', models.TextField(verbose_name='aciklama')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='sahip')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
