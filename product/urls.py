from django.urls import path
from .views import ProductCollectionView, ProductItemView

urlpatterns = [
    path("create/", ProductCollectionView.as_view(), name="product-create"),
    path("list/", ProductCollectionView.as_view(), name="product-list"),
    path("<int:pk>/details/", ProductItemView.as_view(), name="product-details"),
    path("<int:pk>/update/", ProductItemView.as_view(), name="product-update"),
    path("<int:pk>/delete/", ProductItemView.as_view(), name="product-delete"),
]
