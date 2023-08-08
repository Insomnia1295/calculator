from django.urls import path
from . import views

urlpatterns = [
    path('calculator/', views.CalculatorAPI.as_view(), name='api-calculator'),
]
