from django.urls import path

from .views import (
    superuser_view,
    AddNewsView,
    ListNewsView,
    DetailNewsView,
    UpdateNewsView,
    DeleteNewsView,
    register_view,

)

urlpatterns = [
    path('add/', AddNewsView.as_view(), name='add_news'),
    path('<int:pk>/', DetailNewsView.as_view(), name='show_news'),
    path('update/<int:pk>/', UpdateNewsView.as_view(), name='update_news'),
    path('delete/<int:pk>/', DeleteNewsView.as_view(), name='delete_news'),
    path('superuser/', superuser_view, name='superuser'),
    path('register/', register_view, name='register'),
    path('', ListNewsView.as_view(), name='list_news'),
]