from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse, get_object_or_404


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


class Review(models.Model):
    RATING = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='reviews', null=True,
                                blank=True, on_delete=models.SET_NULL)
    review_title = models.CharField(max_length=254)
    review_body = models.TextField()
    rating = models.IntegerField(choices=RATING, default=3)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.review_title

    def calculate_ratings(self):
        # Identify product being rated
        product = get_object_or_404(Product, id=self.product.id)
        # Find all reviews for product
        reviews = Review.objects.all().filter(product=self.product)
        # Iterate through all reviews
        count = len(reviews)
        # Calculate avg of all ratings for reviews
        sum = 0
        for rvw in reviews:
            sum += rvw.rating
        # Set avg rating to product
        product.rating = sum/count
        product.save()

    def save(self, *args, **kwargs):
        super().save()
        self.calculate_ratings()
