# Generated by Django 3.2 on 2021-04-20 09:40

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(max_length=254)),
                ('rating', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('origin', django_countries.fields.CountryField(max_length=2)),
                ('region', models.CharField(blank=True, max_length=254, null=True)),
                ('variety', models.CharField(blank=True, max_length=254, null=True)),
                ('process', models.CharField(blank=True, max_length=254, null=True)),
                ('notes', models.CharField(blank=True, max_length=254, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('weight', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
            ],
        ),
    ]
