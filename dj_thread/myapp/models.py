from django.db import models
from django.db.models.fields.files import ImageField

class Uploads(models.Model):
    image = models.ImageField(upload_to='uploads')