# Generated by Django 3.1.7 on 2021-04-04 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0008_auto_20210404_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('product', models.ManyToManyField(related_name='categories', related_query_name='category', to='learning.Product')),
            ],
        ),
    ]
