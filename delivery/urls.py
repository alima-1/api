from django.urls import path
from .views import DeliveryCollectionView, DeliveryItemView

urlpatterns = [
    path("create/", DeliveryCollectionView.as_view(), name="delivery-create"),
    path("list/", DeliveryCollectionView.as_view(), name="delivery-list"),
    path("<int:pk>/details/", DeliveryItemView.as_view(), name="delivery-details"),
    path("<int:pk>/update/", DeliveryItemView.as_view(), name="delivery-update"),
    path("<int:pk>/delete/", DeliveryItemView.as_view(), name="delivery-delete"),
]
