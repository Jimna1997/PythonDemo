from django.shortcuts import render,redirect,get_object_or_404
from ecommerceapp.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist

def _cart_id(request):
    cart=request.session.session_key
    print(cart)
    if not cart:
        cart=request.session.create()
        print('hrlo')
    return cart

def add_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        print("Add cart")
        print(cart)
    except Cart.DoesNotExist:
        cart=Cart.objects.create(
            cart_id=_cart_id(request)
        )
    cart.save()
    try:
        cart_item=CartItem.objects.get(product=product,cart=cart)
        print(cart_item)
        print(cart_item.quantity)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        print(cart_item.quantity)
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        print(cart_item)
        cart_item.save()
    return redirect('cart_app:cart_detail')

def cart_detail(request,total=0,counter=0,cart_items=None):
    try:
        cart=Cart.objects.get(cart_id=_cart_id(request))
        print('details')
        # print(cart)
        cart_items=CartItem.objects.filter(cart=cart,active=True)
        for cart_item in cart_items:
            total+=(cart_item.product.price * cart_item.quantity)
            print(total)
            counter += cart_item.quantity
            print(counter)
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))

def cart_remove(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product = Product.objects.get(id=product_id)
    print('remove')
    print(product)
    # product=get_object_or_404(Product,id=product_id)
    cart_item=CartItem.objects.get(product=product,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.save()
    return redirect('cart_app:cart_detail')

def full_remove(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product = Product.objects.get(id=product_id)
    cart_item=CartItem.objects.get(product=product,cart=cart)
    cart_item.delete()
    return redirect('cart_app:cart_detail')
