from django.conf import settings
from django.db import models
from django.utils.html import mark_safe

from django.core.validators import FileExtensionValidator


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class DocumentUploadModel(TimeStampedModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    upload_date = models.DateTimeField()
    format = models.FileField(upload_to="images/uploads/%Y/%m/%d", validators=[FileExtensionValidator( ['pdf', 'docx', 'txt'] ) ])
    user = models.IntegerField()


    def __str__(self):
        return self.title

