from unicodedata import category
from rest_framework import serializers
from .models import Category, Item, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Item
        fields = ["name", "category", "image_url"]

    def create(sefl, validated_data):
        print(validated_data)
        category = validated_data.pop('category')
        category = Category.objects.get(name=category['name'])

        item = Item.objects.create(category=category, **validated_data)
        item.save()

        return item


class OrderSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ["delivery_address", "order_date", "item"]

class ItemOrderSerializer(serializers.ModelSerializer):
    item = ItemSerializer()
    order = OrderSerializer()
    class Meta:
        model = Order
        fields = ["order", "item", "item_count"]