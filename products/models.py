from django.db import models
from django_countries.fields import CountryField


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    origin = CountryField(blank_label='Country *', null=False, blank=False)
    region = models.CharField(max_length=254, null=True, blank=True)
    variety = models.CharField(max_length=254, null=True, blank=True)
    process = models.CharField(max_length=254, null=True, blank=True)
    notes = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    weight = models.IntegerField(null=False, blank=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
