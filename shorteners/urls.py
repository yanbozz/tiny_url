from django.urls import path
from .views import UrlView

urlpatterns = [
    path('list', UrlView.as_view(), name='url-list')
]