from django.shortcuts import render,HttpResponse,redirect
from blog.models import Post,BlogComments
from django.contrib import messages
from blog.templatestags import extras


def bloghome(request):
    allPosts =  Post.objects.all()    
    context = {'allPosts': allPosts} 
    return render(request,'blog/bloghome.html',context)

def blogpost(request,slug):
    print(slug)
    if slug == "postComment":
        postcomment(request)
    print("YOU ARE IN POSTCOMMENT 0123")
    post = Post.objects.filter(slug = slug).first() 
    #print(post)
    #print("AAAAAAAAAAAAAAAAAAAAAAAAAAA")
    comments = BlogComments.objects.filter(post=post, parent=None) 
    #replies = BlogComments.objects.filter(post=post).exclude(parent=None) 
    #repDict = {}
    #for reply in replies:
        #if reply.parent.sno not in repDict.keys():
            #repDict[reply.parent.sno] = [reply]
        #else:
            #repDict[reply.parent.sno].append(reply)    'repDict': repDict
    context = {'post':post, 'comments':comments,'user':request.user}
    return render(request,'blog/blogpost.html',context) 
    #return HttpResponse(f'This is blogpost: {slug}')


def postcomment(request):
    print("YOU ARE IN POSTCOMMENT 123 hello")
    if request.method == "POST":
        comment = request.POST.get("comment")
        user = request.user
        postSno = request.POST.get("postSno")
        #print(postSno)
        post = Post.objects.get(sno = postSno) 
        #print(post)
        #print("above post")
        #print(Post.sno)
        #print("post.so")
        parentsno =request.POST.get("Psno")
        user = request.user
        #print(parentsno)
        #print("111111111111111111111111")
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno = postSno)  
        if len(comment)<2:
            messages.error(request,"You give too short comment")
            return redirect(f"/blog/{post.slug}")
        if parentsno ==None:  
            comment = BlogComments(comment=comment,user=user,post=post)
            comment.save()    
            messages.success(request,"Your commment has been posted sucecessfully")
        else:
            parent = BlogComments.objects.get(sno=parentsno)
            #print(parent)
            comment = BlogComments(comment=comment,user=user,post=post,parent=parent)
            messages.success(request,"Your Reply has been posted sucecessfully")
            comment.save()           
    return redirect(f"/blog/{post.slug}")