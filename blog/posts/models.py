from django.db import models
from common.models import Category
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_featured = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category)
    userId = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.title