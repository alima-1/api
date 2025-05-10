from django.urls import path
from .views import SettlementCollectionView, SettlementItemView

urlpatterns = [
    path("create/", SettlementCollectionView.as_view(), name="settlement-create"),
    path("list/", SettlementCollectionView.as_view(), name="settlement-list"),
    path("<int:pk>/details/", SettlementItemView.as_view(), name="settlement-details"),
    path("<int:pk>/update/", SettlementItemView.as_view(), name="settlement-update"),
    path("<int:pk>/delete/", SettlementItemView.as_view(), name="settlement-delete"),
]
