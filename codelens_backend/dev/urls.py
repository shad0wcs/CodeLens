from django.contrib import admin
from django.urls import path, include
from .views import TestTesseractView

app_name = 'dev'

urlpatterns = [
    path('', TestTesseractView.as_view(), name='test-tesseract')
]
