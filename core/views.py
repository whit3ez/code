from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView
from core import models
# Create your views here.
def product_list(request):
    products = models.Product.objects.all()
    return render(request, 'core/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(models.Product, pk=pk)
    return render(request, 'core/product_detail.html', {'product': product})

def category_list(request):
    categories = models.ProductCategory.objects.all()
    return render(request, 'core/category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(models.ProductCategory, pk=pk)
    return render(request, 'core/category_detail.html', {'category': category})

def client_list(request):
    clients = models.Client.objects.all()
    return render(request, 'core/client_list.html', {'clients': clients})

def client_detail(request, pk):
    client = get_object_or_404(models.Client, pk=pk)
    return render(request, 'core/client_detail.html', {'client': client})

def order_list(request):
    orders = models.Order.objects.all()
    return render(request, 'core/order_list.html', {'orders': orders})

def order_detail(request, pk):
    order = get_object_or_404(models.Order, pk=pk)
    return render(request, 'core/order_detail.html', {'order': order})

class ProductListView(ListView):
    model = models.Product
    template_name = 'core/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = models.Product
    template_name = 'core/product_detail.html'
    context_object_name = 'product'

class CategoryListView(ListView):
    model = models.ProductCategory
    template_name = 'core/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(DetailView):
    model = models.ProductCategory
    template_name = 'core/category_detail.html'
    context_object_name = 'category'

class ClientListView(ListView):
    model = models.Client
    template_name = 'core/client_list.html'
    context_object_name = 'clients'

class ClientDetailView(DetailView):
    model = models.Client
    template_name = 'core/client_detail.html'
    context_object_name = 'client'

class OrderListView(ListView):
    model = models.Order
    template_name = 'core/order_list.html'
    context_object_name = 'orders'

class OrderDetailView(DetailView):
    model = models.Order
    template_name = 'core/order_detail.html'
    context_object_name = 'order'
