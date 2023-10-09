

from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('userproducts', UserProductList.as_view(), name='userproducts'),
    path('product_detail/<int:pk>', ProductByName.as_view(), name='detail'),
    path('products', ProductListView.as_view(), name='products'),
    path('categories', CategoryListView.as_view(), name='categories'),
    path('product_by_category/<int:pk>', ProductByCategory.as_view(), name='product_category'),
    path('userproductcreate', UserProductCreate, name='userproductcreate'),
    path('deleteproduct/<int:pk>', deleteproduct, name='delete')
]
