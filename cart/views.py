from django.shortcuts import render, redirect

# Create your views here.

def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    customtext = None
    if 'product_customtext' in request.POST:
        customtext = request.POST['product_customtext']
    cart = request.session.get('cart', {})


    if customtext:
        if item_id in list(cart.keys()):
            if customtext in cart[item_id]['items_by_customtext'].keys():
             cart[item_id]['items_by_customtext'][customtext] += quantity
            else:
                cart[item_id]['items_by_customtext'][customtext] = quantity
        else:
            cart[item_id] = {'items_by_customtext': {customtext: quantity}}
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity



    request.session['cart'] = cart
    return redirect(redirect_url)    

def adjust_bag(request, item_id):
    """ADD SOMETHING HERE"""

    quantity = int(request.POST.get('quantity'))
    customtext = None
    if 'product_customtext' in request.POST:
        customtext = request.POST['product_customtext']
    cart = request.session.get('cart', {})

    if customtext:
        if quantity > 0:
            cart[item_id]['items_by_customtext'][customtext] = quantity
        else:
            del cart[item_id]['items_by_customtext'][customtext]
            if not cart[item_id]['items_by_customtext']:
                cart.pop(item_id)
    else:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop(item_id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        customtext = None
        if 'product_customtext' in request.POST:
            customtext = request.POST['product_customtext']
        cart = request.session.get('cart', {})

        if customtext:
            del cart[item_id]['items_by_customtext'][customtext]
            if not cart[item_id]['items_by_customtext']:
                cart.pop(item_id)
        else:
            cart.pop(item_id)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)