from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['title', 'description', 'customer', 'executor', 'status']
        read_only_fields = ['customer', 'executor', 'status']