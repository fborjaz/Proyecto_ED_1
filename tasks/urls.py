from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from tasks.views import ItemViewSet
from tasks import views

# api versioning
router = routers.DefaultRouter()  
router.register(r'tasks', views.ItemViewSet, 'task')

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
