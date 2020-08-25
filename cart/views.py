from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.

def view_cart(request):
    """ Render the cart contents page """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the product to the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    customtext = None
    customtext2 = None
    customtext3 = None
    if 'product_customtext' in request.POST:
        customtext = request.POST['product_customtext']
    cart = request.session.get('cart', {})
    if 'product_customtext2' in request.POST:
        customtext = request.POST['product_customtext2']
    cart = request.session.get('cart', {})
    if 'product_customtext3' in request.POST:
        customtext = request.POST['product_customtext3']
    cart = request.session.get('cart', {})

    if customtext:
        if item_id in list(cart.keys()):
            if customtext in cart[item_id]['items_by_customtext'].keys():
             cart[item_id]['items_by_customtext'][customtext] += quantity
             messages.success(request, f'Updated product with text {customtext.upper()} {product.name} quantity to {cart[item_id]["items_by_customtext"][customtext]}')
            else:
                cart[item_id]['items_by_customtext'][customtext] = quantity
                messages.success(request, f'Added text {customtext.upper()} {product.name} to your cart')
        else:
            cart[item_id] = {'items_by_customtext': {customtext: quantity}}
            messages.success(request, f'Added product with text {customtext.upper()} {product.name} to your cart')
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to your cart')



    request.session['cart'] = cart
    return redirect(redirect_url)    

def adjust_cart(request, item_id):
    """ Amend shopping cart and update or remove products"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    customtext = None
    if 'product_customtext' in request.POST:
        customtext = request.POST['product_customtext']
    cart = request.session.get('cart', {})

    if customtext:
        if quantity > 0:
            cart[item_id]['items_by_customtext'][customtext] = quantity
            messages.success(request, f'Updated product with text {customtext.upper()} {product.name} quantity to {cart[item_id]["items_by_customtext"][customtext]}')
        else:
            del cart[item_id]['items_by_customtext'][customtext]
            if not cart[item_id]['items_by_customtext']:
                cart.pop(item_id)
            messages.success(request, f'Removed product with text {customtext.upper()} {product.name} from your cart')
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove item from shopping cart"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        customtext = None
        if 'product_customtext' in request.POST:
            customtext = request.POST['product_customtext']
        cart = request.session.get('cart', {})

        if customtext:
            del cart[item_id]['items_by_customtext'][customtext]
            if not cart[item_id]['items_by_customtext']:
                cart.pop(item_id)
            messages.success(request, f'Removed product with text of {customtext.upper()} {product.name} from your cart')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')
        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)