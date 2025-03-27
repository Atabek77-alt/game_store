from django.db import models
from ..product.models import Game

class Cart(models.Model):
    games = models.ManyToManyField(Game, through='CartItem', related_name='cart_game')
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='user_cart')
    total_price = models.DecimalField('Общая цена', max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина пользователя'


    def calculate_total_price(self):
        total = 0

        for item in self.cart_item.all():
            total += item.game.price * item.quantity
        self.total_price = total
        self.save()
        return self.total_price



class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_item')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='game_cart_item')
    quantity = models.PositiveIntegerField('Количество', default=0)

    def __str__(self):
        return f'Игра {self.game.title} в корзине '




