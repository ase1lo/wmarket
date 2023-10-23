from rest_framework import serializers
from shop.models import UserProduct

class UserProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'product',
            'price',
            'quantity',
            'user',
            'want'
        )
        model = UserProduct
