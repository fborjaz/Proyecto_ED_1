from django.contrib import admin
from .models import Item, ShoppingList, ListItems

# Register your models here.

admin.site.register(Item)
admin.site.register(ShoppingList)
admin.site.register(ListItems)

