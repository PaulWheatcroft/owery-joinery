from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
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
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    style = models.ForeignKey(
        'Style', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    description = models.TextField()
    is_offer = models.BooleanField(default=False)
    is_discontinued = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    height = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
