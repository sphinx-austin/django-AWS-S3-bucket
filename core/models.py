from django.db import models

# Create your models here.


# Example PRODUCT model


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='product_images/', default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name