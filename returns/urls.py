from django.urls import path
from .views import ReturnCollectionView, ReturnItemView

urlpatterns = [
    path('create/', ReturnCollectionView.as_view(), name='return-create'),
    path('list/', ReturnCollectionView.as_view(), name='return-list'),
    path('<int:pk>/details/', ReturnItemView.as_view(), name='return-details'),
    path('<int:pk>/update/', ReturnItemView.as_view(), name='return-update'),
    path('<int:pk>/delete/', ReturnItemView.as_view(), name='return-delete'),
]
