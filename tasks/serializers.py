from rest_framework import serializers
from .models import Item, ShoppingList, ListItems

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = '__all__'

class ListItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListItems
        fields = '__all__'
