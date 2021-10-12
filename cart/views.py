from django.shortcuts import render, redirect


def view_cart(request):
    """ A view to return the shopping cart page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    """ Add the quantity of a product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def amend_cart(request,  product_id):
    """ Update the quantity of a product in the shopping cart """

    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart')

    cart[product_id] = quantity

    request.session['cart'] = cart

    return render(request, 'cart/cart.html')


def remove_product_from_cart(request, product_id):
    """ View to add items to a bag """

    cart = request.session.get('cart')

    del cart[product_id]

    request.session['cart'] = cart

    return render(request, 'cart/cart.html')
