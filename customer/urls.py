from django.urls import path
from .views import CustomerCollectionView, CustomerItemView

urlpatterns = [
    path('create/', CustomerCollectionView.as_view(), name='customer-create'),
    path('list/', CustomerCollectionView.as_view(), name='customer-list'),
    path('<int:pk>/details/', CustomerItemView.as_view(), name='customer-details'),
    path('<int:pk>/update/', CustomerItemView.as_view(), name='customer-update'),
    path('<int:pk>/delete/', CustomerItemView.as_view(), name='customer-delete'),
]
