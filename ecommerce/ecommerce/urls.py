from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url,include
from django.contrib import admin
from .views import home_page
# from products.views import (
#     ProductListView,
#     ProductDetailView,
#     ProductDetailSlugView,
#     ProductFeaturedListView,
#     ProductFeaturedDetailView
#     )

urlpatterns = [
    url(r'^$',home_page),
    # url(r'^products/$',ProductListView.as_view()),
    url(r'^products/',include("products.urls",namespace="products")),
    # url(r'^featured/$',ProductFeaturedListView.as_view()),
    # url(r'^featured/(?P<pk>\d+)/$',ProductFeaturedDetailView.as_view()),
    # # url(r'^products/(?P<pk>\d+)/$',ProductDetailView.as_view()),
    # url(r'^products/(?P<slug>[\w-]+)/$',ProductDetailSlugView.as_view()),
    url(r'^admin/', admin.site.urls),
]

if(settings.DEBUG):
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
