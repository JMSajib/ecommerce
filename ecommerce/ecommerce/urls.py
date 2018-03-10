from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from addresses.views import checkout_address_create_view
from accounts.views import login_page,register_page,guest_register_view
from .views import home_page

urlpatterns = [
    url(r'^$',home_page,name="home"),
    url(r'^login/',login_page,name="login"),
    url(r'^logout/',LogoutView.as_view(),name="logout"),
    url(r'^register/guest/',guest_register_view,name="guest_register"),
    url(r'^checkout/address/create/$',checkout_address_create_view,name="checkout_address_create"),
    url(r'^register/',register_page,name="register"),
    url(r'^products/',include("products.urls",namespace="products")),
    url(r'^search/',include("search.urls",namespace="search")),
    url(r'^cart/',include("carts.urls",namespace="cart")),
    url(r'^admin/', admin.site.urls),
]

if(settings.DEBUG):
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
