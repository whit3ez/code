from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('clients/', views.ClientListView.as_view(), name='client_list'),
    path('clients/<int:pk>/', views.ClientDetailView.as_view(), name='client_detail'),
    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('products/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/update/<int:pk>/', views.ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),
]
