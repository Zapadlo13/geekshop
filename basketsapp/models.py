from django.db import models

from authapp.models import User
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    create_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)
    update_datetime = models.DateTimeField(verbose_name='время', auto_now=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def summa(self):
        return self.product.price * self.quantity

    def total_summa(self):
        baskets = Basket.objects.filter(user = self.user)
        return sum( basket.summa() for basket in baskets)

    def total_quantity(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum(basket.quantity for basket in baskets)

    @staticmethod
    def get_item(pk):
        return Basket.objects.get(pk=pk).quantity