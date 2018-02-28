from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView,DetailView
from products.models import Product
# Create your views here.
class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = "products/list.html"

    def get_context_data(self,*args,**kwargs):
        context = super(ProductListView, self).get_context_data(*args,**kwargs)
        return context

class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.featured()

class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.featured()
    template_name = "products/detail.html"

class ProductDetailView(DetailView):
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

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"        
