from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from calculator_app.views import CalculatorView, CalculatorAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculator/', include('calculator_app.urls')),
    path('api/calculator/', CalculatorAPI.as_view(), name='api-calculator'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
