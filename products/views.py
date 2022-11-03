"""Import models"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum, Q
from django.http import HttpResponse
from django.utils.html import escape
from products.forms import CommentProducts
from .models import Product, Comment, Cart
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    """ Render product page """
    pds = Product.objects.all().order_by('product_id')
    return render(request, 'product.html', {'products': pds, 'count': pds.count()})

def product_search(request):
    pds = Product.objects.all()
    if 'pname' in request.GET:
        pname = escape(request.GET["pname"])
        pds = pds.filter(product_name__icontains=pname)

    return render(request, 'product.html', {'products': pds, 'count': pds.count()})

def product_details(request, pid):
    in_cart = Cart.objects.filter(user=request.user.username, product_id=pid).values('product_id', 'user').annotate(quantity=Sum('quantity'))
    quantity = 0
    if in_cart:
        quantity = in_cart.get(product_id=pid).get('quantity')
    comment = Comment.objects.filter(product_id=pid)
    product = Product.objects.get(product_id=pid)
    idproduct = get_object_or_404(Product, product_id=pid)
    form = CommentProducts()
    if request.method == 'POST':
        form = CommentProducts(request.POST, user=request.user, product_id=idproduct)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, 'product_details.html', {'product': product, 'comment': comment, 'form':form, 'quantity': quantity})

def cart_get(request):
    cart = Cart.objects.filter(user=request.user.username).select_related('product_id')
    stock_changed = False
    total_price = 0
    for item in cart:
        in_stock = item.product_id.quantity_in_stock
        # If empty stock, remove entry from cart
        if in_stock == 0:
            Cart.objects.filter(user=request.user.username, product_id=item.product_id).delete()
            stock_changed = True
        # Else, change the quantity of that entry in cart
        elif item.quantity > in_stock:
            Cart.objects.filter(user=request.user.username, product_id=item.product_id).update(quantity=in_stock)
            stock_changed = True

        total_price += item.product_id.sell_price * item.quantity

    return render(request, 'cart.html', {'cart': cart, 'changed': stock_changed, 'total': total_price})

