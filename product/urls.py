
from django.urls import path, include
from .views import ProductView

urlpatterns = [
    path('api', ProductView.as_view()),
]