from django import forms
from django.core.validators import FileExtensionValidator

class UploadPNGForm(forms.Form):
    file = forms.ImageField(label='Загрузите файл:', validators=[FileExtensionValidator,])
