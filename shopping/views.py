from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework import generics
from .models import Item, ShoppingList, ListItems
from .serializers import ItemSerializer, ShoppingListSerializer, ListItemsSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ShoppingListList(generics.ListCreateAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer

class ShoppingListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer

class ListItemsList(generics.ListCreateAPIView):
    queryset = ListItems.objects.all()
    serializer_class = ListItemsSerializer

class ListItemsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListItems.objects.all()
    serializer_class = ListItemsSerializer

