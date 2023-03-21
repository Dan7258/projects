from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True) # максимальное количество символов
    description = models.TextField(null = True, blank=True) # заполнять необязательно

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null = True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=4) # кол-во цифр до запятой и после
    quantity = models.PositiveIntegerField(default = 0) #кол-во товаров на складе по умолчанию 0
    image = models.ImageField(upload_to= 'products_images')
    category = models.ForeignKey(to=ProductCategory, on_delete = models.PROTECT)# категория товара. Связали с другим классом. Что делать при удалении

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name}'
