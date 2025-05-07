from django.urls import path
from .views import OrderCollectionView, OrderItemView, OrderItemCollectionView, OrderItemDetailView

urlpatterns = [
    path('create/', OrderCollectionView.as_view(), name='order-create'),
    path('list/', OrderCollectionView.as_view(), name='order-list'),
    path('<int:pk>/details/', OrderItemView.as_view(), name='order-details'),
    path('<int:pk>/update/', OrderItemView.as_view(), name='order-update'),
    path('<int:pk>/delete/', OrderItemView.as_view(), name='order-delete'),
    path('order-items/', OrderItemCollectionView.as_view(), name='orderitem-collection'),
    path('order-items/<int:pk>/', OrderItemDetailView.as_view(), name='orderitem-detail'),
]
