
from django.conf.urls import url

from .views import (
    cart_page,
    cart_update
    )

urlpatterns = [
    url(r'^$',cart_page,name="home"),
    url(r'^update/$',cart_update,name="update"),
]
