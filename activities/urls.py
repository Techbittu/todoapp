from django.urls import path
from .views import (
    ActivityListView,
    ActivityUpdateView,
    ActivityCreateView,
    ActivityDetailView,
    ActivityDeleteView,
    DeleteManyActivieties,
    ChangeStatusActivieties
)

urlpatterns = [
    path('', ActivityListView.as_view(), name='activity'),
    path('add/', ActivityCreateView.as_view(), name='activity-add'),
    path('<int:pk>/', ActivityDetailView.as_view(), name='activity-detail'),
    path('<int:pk>/update/', ActivityUpdateView.as_view(), name='activity-update'),
    path('<int:pk>/delete/', ActivityDeleteView.as_view(), name='activity-delete'),
    path('delete_many/', DeleteManyActivieties.as_view(), name='activity-delete-many'),
    path('change/<int:pk>', ChangeStatusActivieties.as_view(), name='activity-change'),
]