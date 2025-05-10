from django.urls import path
from .views import VendorCollectionView, VendorItemView

urlpatterns = [
    path("create/", VendorCollectionView.as_view(), name="vendor-create"),
    path("list/", VendorCollectionView.as_view(), name="vendor-list"),
    path("<int:pk>/details/", VendorItemView.as_view(), name="vendor-details"),
    path("<int:pk>/update/", VendorItemView.as_view(), name="vendor-update"),
    path("<int:pk>/delete/", VendorItemView.as_view(), name="vendor-delete"),
]
