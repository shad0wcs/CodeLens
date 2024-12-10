"""Формы для обработки изображений на главной странице."""
from django import forms
from django.core.validators import FileExtensionValidator


class UploadPNGForm(forms.Form):
    """
    Основная форма для обработки изображений.

    Содержит только поле-изображение
    с валидаторам на соответсвие формату
    """

    file = forms.ImageField(label='Загрузите файл:', validators=[FileExtensionValidator,])
