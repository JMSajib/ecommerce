
from django.conf.urls import url

from .views import (
    cart_page,
    cart_update,
    checkout_home,
    checkout_done_view
    )

urlpatterns = [
    url(r'^$',cart_page,name="home"),
    url(r'^checkout/success/$',checkout_done_view,name="success"),
    url(r'^checkout/$',checkout_home,name="checkout"),
    url(r'^update/$',cart_update,name="update"),
]
