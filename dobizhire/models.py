from django.db import models
from django.utils.timezone import now
# Create your models here.

class PostJobs(models.Model):
    jobrole = models.CharField(max_length=200,null=True,blank=True)
    jobcategory = models.CharField(max_length=200,null=True,blank=True)
    exp = models.CharField(max_length=200,null=True,blank=True)
    qualification = models.CharField(max_length=200,null=True,blank=True)
    desc = models.TextField(null=True,blank=True)
    postdate = models.DateTimeField(blank=True,default=now)
    location = models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.jobrole

class AppliedForJobs(models.Model):
    jobrole = models.ForeignKey(to=PostJobs, on_delete=models.CASCADE,null=True,blank=True)
    fname = models.CharField(max_length=200,null=True,blank=True)
    lname = models.CharField(max_length=200,null=True,blank=True)
    email = models.CharField(max_length=200,null=True,blank=True)
    phone = models.CharField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    city = models.CharField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    files = models.FileField(upload_to='CV',null=True,blank=True)
    msg = models.TextField(null=True,blank=True)

    def __str__(self):
        return f'Name =:- {self.fname} from Email:-{self.email}'