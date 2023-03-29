from django.db import models

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