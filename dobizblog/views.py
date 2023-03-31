from django.shortcuts import render, redirect
from dobiz.forms import *
from dobiz.models import *
from .models import *
from django.contrib import messages
#extras
from dobiz.templatetags import extras
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
    comments= BlogComment.objects.filter(post=post, parent=None)
    replies= BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    if request.method == 'POST':
        form = ContactUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('bloghome')
        else:
            form = ContactUser()
    context={'banner':banner,'price':price,'form':form,'post':post,'comments':comments,'replyDict': replyDict}
    return render(request, 'blogpost.html',context)

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

# from django_comments_xtd.models import XtdComment
# from django_comments_xtd.forms import XtdCommentForm

# def blogpost(request,pk):
#     form = ContactUser()
#     banner = Banner.objects.get(category='CommonBanner')
#     price = PricingSum.objects.get(category='Common Price')
#     post = Post.objects.get(sno=pk)
#     if request.method == 'POST':
#         form = ContactUser(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your message has been sent successfully!')
#             return redirect('bloghome')
#         else:
#             form = ContactUser()
#     comments = XtdComment.objects.filter(
#         is_public=True,
#         is_removed=False,
#         object_pk=post.pk,
#         content_type__model=post.__class__.__name__.lower()
#     )
#     comment_form = XtdCommentForm(target_object=post)
#     context = {
#         'banner': banner,
#         'price': price,
#         'form': form,
#         'post': post,
#         'comments': comments,
#         'comment_form': comment_form,
#     }
#     return render(request, 'blogpost.html', context)
