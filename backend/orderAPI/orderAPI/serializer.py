from rest_framework import serializers
from orderApp.models import OrderModel


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderModel
        fields = ['contact_bio', 'adress', 'created_at']
