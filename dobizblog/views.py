from django.shortcuts import render, redirect
from dobiz.forms import *
from dobiz.models import *
from .models import *
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse
#extras
from dobiz.templatetags import extras
# Create your views here.


def blog(request):
    allpage=Page.objects.all()
    category = Category.objects.all()
    blogs = BlogPage.objects.all()
    post = Post.objects.all()
    return render (request,'blog.html', {'category':category, 'blogs':blogs, 'allpage':allpage})

def blog_post(request, page):
    allpage=Page.objects.all()
    category = Category.objects.all()
    blogs = BlogPage.objects.all()
    blog_page = BlogPage.objects.get(page=page)
    blog_for_heading = BlogPage.objects.get(page=page)
    post = Post.objects.filter(page=blog_page).order_by('-timestap')[0:6]
    total_obj = Post.objects.count()
    return render(request, 'blog.html', {'category': category, 'blogs': blogs, 'post': post,'total_obj':total_obj,'blog_for_heading':blog_for_heading,'allpage':allpage})

def load_more(request):
    total_item = int(request.GET.get('total_item'))
    limit = 6
    pagename = request.GET.get('page')
    blog_page = BlogPage.objects.get(page=pagename)
    post_obj = list(Post.objects.filter(page=blog_page).order_by('-timestap').values()[total_item:total_item+limit])
    data = {
        'posts':post_obj,
    }
    return JsonResponse(data=data)



def oneblog(request, pk):
    allpage=Page.objects.all()
    post = Post.objects.get(sno=pk)
    pages = BlogPage.objects.all()
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    # Get recent posts
    recent_posts = Post.objects.filter(timestap__lte=timezone.now()).exclude(pk=post.pk).order_by('-timestap')[:5]

    return render(request, 'oneblog.html', {'post': post, 'comments': comments, 'replyDict': replyDict, 'pages': pages, 'recent_posts': recent_posts,'allpage':allpage})



def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            comment=BlogComment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment= comment, user=user, post=post , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
        
    return redirect(f"/blogpost/{post.sno}")

