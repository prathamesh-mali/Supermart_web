from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Product, Category, Order, Feedback
from django.contrib.auth.models import User


# Create your views here.

# Home page view


def home(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}

    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'products': products,
        'categories': categories

    }
    return render(request, 'index.html', context)


def searchMatch(query, item):
    if query in item.desc.lower() or query in item.name.lower() or query in item.category.name.lower():
        return True
    else:
        return False
    if Category.objects.filter(category__name=name):
        return True
    else:
        return False


def search(request):
    categories = Category.objects.all()
    query = request.GET.get('search').lower()
    print(query)
    products = Product.objects.all()
    product = [item for item in products if searchMatch(query, item)]
    prodlen = len(product)
    data = {
        'products': product,
        'categories': categories
    }
    return render(request, 'search.html', data)


# All product view
def allproducts(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    cat = {
        'categories': categories,
        'products': products
    }
    return render(request, 'products.html', cat)

# Cart View


def cart(request):
    categories = Category.objects.all()
    ids = list(request.session.get('cart').keys())
    products = Product.get_product_by_id(ids)
    print(products)

    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'cart.html', context)

# feedback View


def feedback(request):
    if request.method == 'POST':
        full_name = request.POST['name']
        subject = request.POST['sub']
        desc = request.POST['desc']
        print(full_name, subject, desc)
        ins = Feedback(
            name=full_name,
            subject=subject,
            description=desc
        )
        ins.save()
    return render(request, 'feedback.html')


# Product info page view

def productinfo(request, prodid):
    categories = Category.objects.all()
    products = Product.objects.all()
    product = Product.objects.filter(id=prodid)
    addProduct = request.POST.get('productInCart')
    remove = request.POST.get('remove')
    cart = request.session.get('cart')

    if addProduct:
        if cart:
            quantity = cart.get(addProduct)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(addProduct)
                    else:
                        cart[addProduct] = quantity - 1
                else:
                    cart[addProduct] = quantity + 1
            else:
                cart[addProduct] = 1
        else:
            cart = {}
            cart[addProduct] = 1

    request.session['cart'] = cart

    prodcontext = {
        'product': product[0],
        'products': products,
        'categories': categories,

    }
    return render(request, 'productinfo.html', prodcontext)


# product based on category view
def catProd(request, catid):
    categories = Category.objects.all()
    products = Product.objects.all()
    category_with_Id = Category.objects.filter(id=catid)
    catProd = {
        'category_with_Id': category_with_Id[0],
        'categories': categories,
        'products': products,

    }
    return render(request, 'catProd.html', catProd)


def checkout(request):
    Phone = request.POST.get('Contact')
    address = request.POST.get('Address')
    user = request.user
    cart = request.session.get('cart')
    products = Product.get_product_by_id(list(cart.keys()))

    for product in products:
        order = Order(user=user, product=product,
                      price=product.price, quantity=cart.get(str(product.id)), address=address, phone=Phone)

    order.placeorder()
    request.session['cart'] = {}
    return redirect('order')


def order(request):
    cart = request.session.get('cart')
    customer = request.user.id
    order = Order.get_orders_by_customer(customer)
    lenCart = len(cart)
    print(order)
    return render(request, 'order.html', {'lenCart': lenCart, 'orders': order})
