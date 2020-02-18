from django.db import models
from common.models import Category
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_featured = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category)
    def __str__(self):
        return self.title