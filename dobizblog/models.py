from django.db import models
from dobiz.models import User
from django.utils.timezone import now
# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)
    timestap = models.DateTimeField(blank=True)
    img = models.ImageField(null=True, blank=True)
    colorcode1 = models.CharField(max_length=200,null=True, blank=True, default='#90cd26')
    colorcode2 = models.CharField(max_length=200,null=True, blank=True, default='#1742fd')
    
    def __str__(self):
        return self.title + " "+ "by" + " "+ self.author


class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)
    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.fname

