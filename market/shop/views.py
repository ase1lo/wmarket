from typing import Any, Dict
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Product, UserProduct, Category
from .forms import UserProductForm
# Create your views here.



class UserProductList(ListView):
    model = UserProduct
    template_name = 'market/userproduct.html'
    context_object_name = 'userpoducts'


class ProductByName(DetailView):
    model = Product
    template_name = 'market/product_detail.html'
    context_object_name = 'products'
    
    def get(self, request, *args, **kwargs):
        product_pk = kwargs['pk']
        request.session['pk'] = product_pk

        try:
            self.userproduct = UserProduct.objects.filter(product_id=product_pk)
        except:
            pass
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['userproducts'] = self.userproduct
        return data
    
    
class ProductListView(ListView):
    model = Product
    template_name = 'market/mainpage.html'
    context_object_name = 'products'


class CategoryListView(ListView):
    model = Category
    template_name = 'category/category.html'
    context_object_name = 'categories'


class ProductByCategory(ListView):
    model = Product
    template_name = 'category/product_category.html'
    context_object_name = 'products'

    def get(self, request, *args, **kwargs):
        cat_pk = kwargs['pk']
        try:
            self.cat_product = Product.objects.filter(category_id = cat_pk)
        except:
            pass
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['cat_product'] = self.cat_product
        print(data)
        return data
    

def UserProductCreate(request):
    if request.method == 'POST':
        user = request.user
        product = request.session.get('pk')
        form = UserProductForm(request.POST)
        if form.is_valid():
            user_product = form.save(commit=False)
            user_product.product = Product.objects.get(pk=product)
            user_product.user = user
            user_product.save()
            return redirect('products')
    else:
        form = UserProductForm()

    return render(request, 'market/userproductform.html', {'form': form})


def deleteproduct(request, *args, **kwargs):
    context = {}
    id = kwargs['pk']
    obj = get_object_or_404(UserProduct, id=id)
    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect('/market/products')
    
    return render(request, 'market/deleteproduct.html', context)

