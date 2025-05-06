from django.urls import path
from .views import CourierCollectionView, CourierItemView

urlpatterns = [
    path('create/', CourierCollectionView.as_view(), name='courier-create'),
    path('list/', CourierCollectionView.as_view(), name='courier-list'),
    path('<int:pk>/details/', CourierItemView.as_view(), name='courier-details'),
    path('<int:pk>/update/', CourierItemView.as_view(), name='courier-update'),
    path('<int:pk>/delete/', CourierItemView.as_view(), name='courier-delete'),
]
