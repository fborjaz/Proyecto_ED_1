from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class ShoppingList(models.Model):
    name = models.CharField(max_length=100)
    items = models.ManyToManyField(Item, through='ListItems')

    def __str__(self):
        return self.name

class ListItems(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    added_at = models.DateTimeField(auto_now_add=True)


