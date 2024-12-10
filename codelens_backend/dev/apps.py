"""Конфигурация App'а."""
from django.apps import AppConfig


class DevConfig(AppConfig):
    """Конфигурация App'а."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dev'
