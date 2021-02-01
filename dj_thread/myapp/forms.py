from django import forms
from django.db import models
from django.db.models import fields
from .models import Uploads
from django.forms.widgets import ClearableFileInput


class UploadForm(forms.ModelForm):
    class Meta:
        model = Uploads
        fields = ['image']
        widgets = {
            'image': ClearableFileInput(attrs={
                'multiple': True
            }),
            'type': 'jpg/jpeg'
        }
