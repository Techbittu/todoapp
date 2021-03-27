from .views import ActivitiesRudView, ActivitiesView
from django.urls import path


urlpatterns = [
    path('<int:pk>/', ActivitiesRudView.as_view(), name='activity-rud'),
    path('', ActivitiesView.as_view(), name='activity-create'),
]