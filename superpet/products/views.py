from django.shortcuts import render
from .models import Product,Category
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView



# Create your views here.

def products(request):
    return render(request,"products.html")

def royalCanin(request):
    products=Product.CustomManager.Royalcanin()
    return render(request,"products.html",{"products":products})

def pedigree(request):
    products=Product.CustomManager.Pedigree()
    return render(request,"products.html",{"products":products})

def drools(request):
    products=Product.CustomManager.Drools()
    return render(request,"products.html",{"products":products})

def search(request):
    keyword=request.GET.get("keyword")
    products=Product.CustomManager.all().filter(product_name__icontains=keyword)
    return render(request,"products.html",{"products":products})

class ProductListView(ListView):
    model=Product

class ProductDetailView(DetailView):
    model=Product
    template_name="products/productdetail.html"

class ProductCreateView(CreateView):
    model=Product
    fields="__all__"   # fields="list"
    success_url="/products"

class productUpdateView(UpdateView):
    model=Product
    fields="__all__"
    success_url="/products"

class productDeleteView(DeleteView):
    model=Product
    success_url="/products"

class CategoryDetailView(DetailView):
    model=Category
    template_name="category/category_detail.html"
    slug_field="category_slug"
    context_object_name="category_obj"