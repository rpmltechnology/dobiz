from django.db import models
from django.utils.timezone import now
# Create your models here.

class PostJobs(models.Model):
    jobrole = models.CharField(max_length=200,null=True,blank=True)
    jobcategory = models.CharField(max_length=200,null=True,blank=True)
    exp = models.CharField(max_length=200,null=True,blank=True)
    total_openings = models.CharField(max_length=200,null=True,blank=True)
    qualification = models.CharField(max_length=200,null=True,blank=True)
    desc = models.TextField(null=True,blank=True)
    postdate = models.DateTimeField(blank=True,default=now)
    location = models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return self.jobrole

class AppliedForJobs(models.Model):
    jobrole = models.ForeignKey(to=PostJobs, on_delete=models.CASCADE,null=True)
    fname = models.CharField(max_length=200,null=True)
    lname = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    files = models.FileField(upload_to='CV-Resumes/',max_length=500,null=True)
    msg = models.TextField(null=True,blank=True)

    def __str__(self):
        return f'Name:- {self.fname} from Email:-{self.email}'