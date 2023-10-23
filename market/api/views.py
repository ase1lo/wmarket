from django.shortcuts import render
from .serializers import UserProductSerializer
from rest_framework import mixins
from rest_framework import generics
from shop.models import UserProduct

# Create your views here.


class UserProductView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = UserProduct.objects.all()
    serializer_class = UserProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    