from django import forms
from django.core.validators import FileExtensionValidator

class UploadPNGForm(forms.Form):
    file = forms.ImageField(label='Image with code snippet', validators=[FileExtensionValidator,])
