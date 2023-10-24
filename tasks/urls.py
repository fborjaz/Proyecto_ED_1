from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.ItemList.as_view(), name='item-list'),
    path('items/<int:pk>/', views.ItemDetail.as_view(), name='item-detail'),
    path('shoppinglists/', views.ShoppingListList.as_view(), name='shoppinglist-list'),
    path('shoppinglists/<int:pk>/', views.ShoppingListDetail.as_view(), name='shoppinglist-detail'),
    path('listitems/', views.ListItemsList.as_view(), name='listitems-list'),
    path('listitems/<int:pk>/', views.ListItemsDetail.as_view(), name='listitems-detail'),
]
