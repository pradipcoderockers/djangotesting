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
    image = models.ImageField(upload_to='upload',null=True,blank=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    post  = models.ForeignKey(Post,on_delete=models.CASCADE,default=1)
    userId  = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    content = models.TextField()
    reply = models.ForeignKey('Comment', null=True, related_name="replies",on_delete=models.CASCADE)
    addedOn = models.DateField(auto_now_add=True)
    def __str__(set):
        return '{}-{}'.format(set.post.title,str(set.user.username))        