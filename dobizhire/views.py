from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
from dobizhire.models import *
from dobizhire.forms import *
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.
##############Hiring#########################

def hire(request):
    post = PostJobs.objects.all()
    return render(request, 'hire.html',{'post':post})

def viewjobs(request, id):
    post = PostJobs.objects.get(id=id)
    return render(request, 'jobs.html', {'post':post})

def opportunities(request,id):
    post = PostJobs.objects.get(id=id)
    if request.method == 'POST':
        form = JobApplication(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('home')
    else:
        form = JobApplication()
    return render (request, 'opportunities.html',{'post':post,'form':form})