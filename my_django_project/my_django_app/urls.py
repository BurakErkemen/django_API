from django.urls import path
from .views import ImageUploadView  # Diğer view'lerinizi de ekleyin

urlpatterns = [
    path('upload/', ImageUploadView.as_view(), name='image-upload'),
    # Diğer endpoint'lerinizi buraya ekleyin
]