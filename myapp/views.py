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
    products = Nutrition.objects.all()  # 获取所有商品
    return render(request, 'myapp/product_list.html', {'products': products})

# ...
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)  # 确保从Product模型获取对象
    request.session['last_product_id'] = id  # 保存最后查看的产品ID
    return render(request, 'myapp/product_detail.html', {'product': product})
# ...


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # 重定向到登录页面注册成功后
    template_name = 'myapp/signup.html'  # 指向使用的模板

@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'myapp/cart.html', {'cart_items': cart_items})

@login_required  # 确保用户必须登录
@require_POST  # 确保这个视图只能通过POST方法访问
def add_to_cart(request, product_id):
    # 从URL中获得的product_id是用来获取产品对象的
    product = get_object_or_404(Product, id=product_id)
    # 从session中获取或创建购物车项目
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,  # 正确使用request.user表示当前登录的用户
        product=product,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')  # 重定向到购物车页面

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
    products = Product.objects.all().order_by('name')  # 按产品名称排序
    paginator = Paginator(products, 100)  # 创建Paginator对象，每页显示100项

    page = request.GET.get('page')  # 从GET请求中获取页码
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # 如果页码不是整数，展示第一页
        products = paginator.page(1)
    except EmptyPage:
        # 如果页码超出范围，展示最后一页
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
                    # 处理库存不足的情况
                    return HttpResponse("库存不足，无法完成购买。")
        return redirect('cart')
    return redirect('cart')

def advanced_search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        # 根据搜索关键字进行过滤，这里假设产品名称包含关键字即可
        products = Product.objects.filter(name__icontains=keyword)
    else:
        products = Product.objects.all()
    return render(request, 'myapp/product_list.html', {'products': products})