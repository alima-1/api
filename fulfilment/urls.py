from django.urls import path
from .views import FulfilmentCollectionView, FulfilmentItemView

urlpatterns = [
    path('create/', FulfilmentCollectionView.as_view(), name='fulfilment-create'),
    path('list/', FulfilmentCollectionView.as_view(), name='fulfilment-list'),
    path('<int:pk>/details/', FulfilmentItemView.as_view(), name='fulfilment-details'),
    path('<int:pk>/update/', FulfilmentItemView.as_view(), name='fulfilment-update'),
    path('<int:pk>/delete/', FulfilmentItemView.as_view(), name='fulfilment-delete'),
]
