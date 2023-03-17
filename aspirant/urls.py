from django.urls import path

from .views import AspirantListView, TechnologiesListView


urlpatterns = [
    path('api/v1/aspirants/', AspirantListView.as_view(), name='aspirants-list'),
    path('api/v1/technologies/', TechnologiesListView.as_view(), name='technologies-list')
]
