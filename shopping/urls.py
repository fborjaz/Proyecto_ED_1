from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from shopping.views import ItemViewSet
from shopping import views

# api versioning
router = routers.DefaultRouter()  
router.register(r'shopping', views.ItemViewSet, 'shopping')

urlpatterns = [
    path("api/v1/", include(router.urls)), 
    path('docs/', include_docs_urls(title='Simulador API', description='RESTful API for Simulador DJ')),
    path('items/', views.ItemList.as_view(), name='item-list'),
    path('items/<int:pk>/', views.ItemDetail.as_view(), name='item-detail'),
    path('shoppinglists/', views.ShoppingListList.as_view(), name='shoppinglist-list'),
    path('shoppinglists/<int:pk>/', views.ShoppingListDetail.as_view(), name='shoppinglist-detail'),
    path('listitems/', views.ListItemsList.as_view(), name='listitems-list'),
    path('listitems/<int:pk>/', views.ListItemsDetail.as_view(), name='listitems-detail'),
]
