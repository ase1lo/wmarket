from django.contrib import admin
from .models import Product, UserProduct, Category

# Register your models here.


admin.site.register(Product)
admin.site.register(UserProduct)
admin.site.register(Category)


