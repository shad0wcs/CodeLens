"""Routes для приложения."""
from django.urls import path

from .views import AboutPage, TestTesseractView

app_name = 'dev'

urlpatterns = [
    path('about/', AboutPage.as_view(), name='about'),
    path('', TestTesseractView.as_view(), name='test-tesseract')
]
