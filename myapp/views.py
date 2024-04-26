from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Nutrition, Product, CartItem
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ProductForm
from django.db import transaction

def product_list(request):
    products = Nutrition.objects.all()  # Get all products
    return render(request, 'myapp/product_list.html', {'products': products})

# ...
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)  # Make sure to get the object from the Product model
    request.session['last_product_id'] = id  # Save the last viewed product ID
    return render(request, 'myapp/product_detail.html', {'product': product})
# ...


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redirect to login page after successful registration
    template_name = 'myapp/signup.html'  # Points to the template used

@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'myapp/cart.html', {'cart_items': cart_items})

@login_required  # Make sure the user must be logged in
@require_POST  # Make sure this view is only accessible through the POST method
def add_to_cart(request, product_id):
    # product_id from the URL is used to get the product object
    product = get_object_or_404(Product, id=product_id)
    # Get or create a shopping cart item from session
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,  # Use request.user correctly to indicate the user currently logged in
        product=product,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')  # Redirect to cart page

@require_POST
@login_required
def update_cart(request):
    item_id = request.POST.get('item_id')
    if 'update' in request.POST:
        quantity = request.POST.get(f'quantity-{item_id}')
        cart_item = CartItem.objects.get(id=item_id, user=request.user)
        cart_item.quantity = int(quantity)
        cart_item.save()
    elif 'remove' in request.POST:
        cart_item = CartItem.objects.get(id=item_id, user=request.user)
        cart_item.delete()
    return redirect('cart')




def product_list(request):
    products = Product.objects.all()
    products = Product.objects.all().order_by('name')  # Sort by product name
    paginator = Paginator(products, 100)  # Create a Paginator object that displays 100 items per page

    page = request.GET.get('page')  # GET page numbers from the GET request
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If the page number is not an integer, show the first page
        products = paginator.page(1)
    except EmptyPage:
        # If the page number is out of range, show the last page
        products = paginator.page(paginator.num_pages)

    return render(request, 'myapp/product_list.html', {'products': products})


def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', id=product.id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'myapp/update_product.html', {'form': form})

def purchase_items(request):
    if request.method == 'POST':
        cart_items = CartItem.objects.filter(user=request.user, is_purchased=False)
        with transaction.atomic():
            for item in cart_items:
                product = item.product
                if product.stock >= item.quantity:
                    product.stock -= item.quantity
                    product.save()
                    item.is_purchased = True
                    item.save()
                else:
                    # Deal with stock shortage
                    return HttpResponse("Insufficient stock to complete the purchase。")
        return redirect('cart')
    return redirect('cart')

def advanced_search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        products = Product.objects.filter(name__icontains=keyword)
    else:
        products = Product.objects.all()
    return render(request, 'myapp/product_list.html', {'products': products})