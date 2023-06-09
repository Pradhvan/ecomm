from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class ActiveProductLineQueryset(models.QuerySet):
    def isactive(self):
        return self.filter(is_active=True)


# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self) -> str:
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self) -> str:
        return self.name


class ProductLine(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sku = models.CharField(max_length=18)
    stock_quantity = models.IntegerField()
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_line"
    )
    is_active = models.BooleanField(default=False)
    objects = ActiveProductLineQueryset.as_manager()

    def __str__(self) -> str:
        return self.sku
