from django.db import models

from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from user.models import User


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class DocumentUploadModel(TimeStampedModel):

    def file_size_validation(value):
        filesize = value.size
        print("filesize", filesize)
        if filesize > 2024894:
            raise ValidationError("File size must be less than 2MB")
        else:
            return value
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    upload_date = models.DateTimeField()
    format = models.FileField(upload_to="images/uploads/%Y/%m/%d", validators=[FileExtensionValidator( ['pdf', 'docx', 'txt']), file_size_validation])
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.title

