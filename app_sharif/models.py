from django.db import models
class slider(models.Model):
    title=models.CharField(max_length=120)
    image=models.ImageField(upload_to='uploads/')
    def __str__(self):
        return self.title
