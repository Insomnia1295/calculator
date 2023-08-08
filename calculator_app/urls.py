from django.urls import path
from .views import CalculatorView
from .api import CalculatorAPI
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('calculator/', CalculatorView.as_view(), name='calculator'),
    path('api', CalculatorAPI.as_view(), name='api-calculator'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
