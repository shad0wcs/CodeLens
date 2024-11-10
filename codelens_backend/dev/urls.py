from django.contrib import admin
from django.urls import path, include
from .views import TestTesseractView, AboutPage, LegacyTestTesseractView

app_name = 'dev'

urlpatterns = [
    path('legacy/', LegacyTestTesseractView.as_view(), name='legacy'),
    path('about/', AboutPage.as_view(), name='about'),
    path('', TestTesseractView.as_view(), name='test-tesseract')
]
