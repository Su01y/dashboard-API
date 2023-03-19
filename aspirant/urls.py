from django.urls import path

from .views import AspirantListView, SelectedAspirants, TechnologiesListView, FilterTechnologies


urlpatterns = [
    path('api/v1/aspirants/', AspirantListView.as_view(), name='aspirants-list'),
    path('api/v1/technologies/', TechnologiesListView.as_view(), name='technologies-list'),
    path('api/v1/aspirants-filter-technologies/', FilterTechnologies.as_view()),
    path('api/v1/aspirants-filter-id/', SelectedAspirants.as_view()),
]
