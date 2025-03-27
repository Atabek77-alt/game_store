from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from .models import Cart, CartItem
from ..blog.models import Post
from ..product.models import Game

class CartGenericView(TemplateView):
    template_name = 'pages/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        action = self.kwargs.get('action')
        cart_item_id = self.kwargs.get('cart_item_id')
        new_quantity = self.request.GET.get('quantity')

        if not self.request.user.is_authenticated:
            return redirect('login')

        cart, created = Cart.objects.get_or_create(user=self.request.user)

        if action == 'add':
            game = get_object_or_404(Game, id=cart_item_id)
            cart_item, created = CartItem.objects.get_or_create(cart=cart, game=game)
            cart_item.quantity += 1
            cart_item.save()

        elif action == 'remove':
            cart_item = CartItem.objects.filter(cart=cart, game_id=cart_item_id).first()
            if cart_item:
                if cart_item.quantity > 1:
                    cart_item.quantity -= 1
                    cart_item.save()
                else:
                    cart_item.delete()


        elif action == 'update' and new_quantity is not None:



            try:

                new_quantity = int(new_quantity)

                if new_quantity > 0:

                    cart_item = CartItem.objects.get(cart=cart, game_id=cart_item_id)

                    cart_item.quantity = new_quantity

                    cart_item.save()

                else:

                    cart_item = CartItem.objects.get(cart=cart, game_id=cart_item_id)

                    cart_item.delete()

            except ValueError:

                pass

        cart_items = CartItem.objects.filter(cart=cart)
        total_price = 0
        for item in cart_items:
            if item.game.price is not None:
                total_price += item.game.price * item.quantity
            else:
                total_price += 0

            item.total_price = item.game.price * item.quantity if item.game.price else 0
            item.save()

        cart.total_price = total_price
        cart.save()

        context['cart'] = cart
        context['cart_items'] = cart_items
        context['posts'] = Post.objects.all().order_by('-created_at')[:3]

        return context
