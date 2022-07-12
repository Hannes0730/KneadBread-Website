import os
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


category_list = {
    ('cake', 'Cake'),
    ('cookies', 'Cookies'),
    ('goodies', 'Goodies'),
    ('muffins', 'Muffins'),
}

def uploadimage(instance, filename):
    return os.path.join(instance.product.slug, filename)



# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-list', kwargs={'name': self.name})


class Reviews(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    review = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(null=False, default="Description Coming Soon!")
    main_image = models.ImageField(null=True,blank=True)
    price = models.DecimalField(decimal_places=2, null=False, max_digits=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Products, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('name', 'slug')

class ProductImage(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    sub_image = models.ImageField(upload_to=uploadimage, null=True,blank=True)

    def __str__(self):
        return str(self.sub_image)
