from django.shortcuts import render,redirect
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
from dobizhire.models import *
from dobizhire.forms import *
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404
import os
# Create your views here.
##############Hiring#########################
def thank(request):
    return render(request,'thank-you.html')

def hire(request):
    post = PostJobs.objects.all()
    return render(request, 'hire.html',{'post':post})

def viewjobs(request, id):
    post = PostJobs.objects.get(id=id)
    return render(request, 'jobs.html', {'post':post})

def opportunities(request, id):
    post = get_object_or_404(PostJobs, id=id)

    if request.method == 'POST':
        form = JobApplication(request.POST, request.FILES)
        if form.is_valid():
            job_application = form.save(commit=False)
            job_application.jobrole = post
            # rename the uploaded file to fname
            job_application.files.name = job_application.fname + os.path.splitext(job_application.files.name)[1]
            job_application.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('dobizhire:thank')
        else:
            messages.error(request, 'Something went wrong')
    else:
        form = JobApplication()

    return render(request, 'opportunities.html', {'post': post, 'form': form})
