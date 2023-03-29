from django.shortcuts import render, redirect
from dobiz.forms import *
from dobiz.models import *
from .models import *
# Create your views here.
def bloghome(request):
    form = ContactUser()
    banner = Banner.objects.get(category='CommonBanner')
    price = PricingSum.objects.get(category='Common Price')
    post = Post.objects.all()
    print(post)
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('bloghome')
        else:
            form = ContactUser()
    context={'banner':banner,'price':price,'form':form,'post':post}

    return render(request, 'bloghome.html',context)

def blogpost(request,pk):
    form = ContactUser()
    banner = Banner.objects.get(category='CommonBanner')
    price = PricingSum.objects.get(category='Common Price')
    post = Post.objects.get(sno=pk)
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('bloghome')
        else:
            form = ContactUser()
    context={'banner':banner,'price':price,'form':form,'post':post}
    return render(request, 'blogpost.html',context)