# Generated by Django 3.1.7 on 2021-04-04 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('learning', '0006_auto_20210404_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('address', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
            ],
        ),
    ]
