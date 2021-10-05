from django.db import models


class Category(models.Model):
    """ product category """
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

    def get_frielndly_name(self):
        return self.friendly_name


class Style(models.Model):
    """ product style """
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

    def get_frielndly_name(self):
        return self.friendly_name


class Product(models.Model):
    """ product details """
    Category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    Style = models.ForeignKey(
        'Style', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    is_offer = models.BooleanField(default=0)
    is_discontinued = models.BooleanField(default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    height = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
