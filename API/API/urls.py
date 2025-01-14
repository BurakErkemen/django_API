from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('API_app.urls')),  # API_app url'lerini dahil edin
]