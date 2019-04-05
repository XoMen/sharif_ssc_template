from django.db import models
from froala_editor.fields import FroalaField
from django.utils.safestring import mark_safe


class slider(models.Model):
    active=models.BooleanField(default="True")
    title=models.CharField(max_length=100 , null="True")
    image=models.ImageField(upload_to='uploads/')
    def __str__(self):
        return self.title

class post(models.Model):
    active=models.BooleanField(default="True")
    image=models.ImageField(upload_to='uploads/')
    title=models.CharField(max_length=100, null="True")
    description=models.TextField(null="True",default="")
    button=models.CharField(max_length=100 ,default="اطلاعات بیشتر ")

    def __str__(self):
        return self.title
