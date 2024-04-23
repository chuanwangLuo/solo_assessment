from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import SignUpView
from .views import cart_view
from .views import add_to_cart
from .views import update_cart
from .views import update_product
from .views import purchase_items
from .views import advanced_search

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('cart/', cart_view, name='cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('update-cart/', update_cart, name='update_cart'),
    path('update-product/<int:id>/', update_product, name='update_product'),
    path('purchase-items/', purchase_items, name='purchase_items'),
    path('advanced-search/', views.advanced_search, name='advanced_search'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)