from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url,include
from django.contrib import admin
from .views import home_page

urlpatterns = [
    url(r'^$',home_page,name="home"),
    url(r'^products/',include("products.urls",namespace="products")),
    url(r'^search/',include("search.urls",namespace="search")),
    url(r'^cart/',include("carts.urls",namespace="cart")),
    url(r'^admin/', admin.site.urls),
]

if(settings.DEBUG):
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
