from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from addresses.views import checkout_address_create_view,checkout_address_reuse_view
from billing.views import payment_method_view,payment_method_create_view
from carts.views import cart_detail_api_view
from accounts.views import LoginView,RegisterView,guest_register_view
from .views import home_page,contact_page

urlpatterns = [
    url(r'^$',home_page,name="home"),
    url(r'^login/',LoginView.as_view(),name="login"),
    url(r'^contact/',contact_page,name="contact"),
    url(r'^logout/',LogoutView.as_view(),name="logout"),
    url(r'^api/cart/$',cart_detail_api_view,name="api_cart"),
    url(r'^register/guest/',guest_register_view,name="guest_register"),
    url(r'^checkout/address/create/$',checkout_address_create_view,name="checkout_address_create"),
    url(r'^checkout/address/reuse/$',checkout_address_reuse_view,name="checkout_address_reuse"),
    url(r'^register/',RegisterView.as_view(),name="register"),
    url(r'^billing/payment/$',payment_method_view,name="payment"),
    url(r'^billing/payment/create/$',payment_method_create_view,name="payment-method-endpoint"),
    url(r'^products/',include("products.urls",namespace="products")),
    url(r'^search/',include("search.urls",namespace="search")),
    url(r'^cart/',include("carts.urls",namespace="cart")),
    url(r'^admin/', admin.site.urls),
]

if(settings.DEBUG):
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
