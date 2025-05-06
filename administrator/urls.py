from django.urls import path
from .views import AdministratorCollectionView, AdministratorItemView

urlpatterns = [
    path('create/', AdministratorCollectionView.as_view(), name='administrator-collection'),
    path('list/', AdministratorCollectionView.as_view(), name='administrator-list'),
    path('<int:pk>/details/', AdministratorItemView.as_view(), name='administrator-details'),
    path('<int:pk>/update/', AdministratorItemView.as_view(), name='administrator-update'),
    path('<int:pk>/delete/', AdministratorItemView.as_view(), name='administrator-delete'),
]
