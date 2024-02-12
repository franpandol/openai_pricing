
from django.urls import path

from . import views

urlpatterns = [
    path('calculate_cost/', views.CostAPIView.as_view(), name='calculate_cost'),
]
