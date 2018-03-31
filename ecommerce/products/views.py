from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView,DetailView
from products.models import Product
from analytics.mixins import ObjectViewedMixin
from carts.models import Cart
# Create your views here.
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_context_data(self,*args,**kwargs):
        context = super(ProductListView,self).get_context_data(*args,**kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.featured()

class ProductFeaturedDetailView(ObjectViewedMixin,DetailView):
    queryset = Product.objects.featured()
    template_name = "products/detail.html"

class ProductDetailView(ObjectViewedMixin,DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self,*args,**kwargs):
        context = super(ProductDetailView, self).get_context_data(*args,**kwargs)
        return context

    def get_object(self,*args,**kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        print(pk)
        instance = Product.objects.get_by_id(pk)
        print(instance)
        if(instance is None):
            raise Http404('Products Not Found')
        return instance

class ProductDetailSlugView(ObjectViewedMixin,DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self,*args,**kwargs):
        context = super(ProductDetailSlugView,self).get_context_data(*args,**kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self,*args,**kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        try:
            instance = Product.objects.get(slug=slug,active=True)
        except Product.DoesNotExist:
            raise Http404("Not found")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug,active=True)
            instance = qs.first()
        except:
            raise Http404("Problem")

        # object_viewed_signal.send(instance.__class__,instance=instance,request=request)
        return instance
