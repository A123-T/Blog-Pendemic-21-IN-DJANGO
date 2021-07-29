from django.shortcuts import render,HttpResponse,redirect
from home.models import contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout
#html pages
def home(request):    
    return render(request,'home/home.html')

def Contact(request):
    messages.success(request, '  Welcome to Contact us.') 
    if request.method == "POST":
        print("WE ARE USING POST REQUEST ") 
        email = request.POST['email']   
        phone = request.POST['phone']   
        query = request.POST['query']  
        print(email,phone,query) 
        if len(email)<3 or len(phone)<10 or query=="":
            messages.error(request, '  Please fill the form Correctly.') 
        else:         
            Contact = contact(email = email, phone =phone, query = query)
            Contact.save()
            messages.info(request, '  Your message has been recieved to admin\nTHANKYOU.') 
    return render(request,'home/contact.html')
    #return HttpResponse('This is contact')

def about(request):   
    messages.success(request, '  Welcome to About us.')  
    return render(request,'home/about.html')
   # return HttpResponse('This is about')

def search(request):
    query = request.GET['query'] 
    if len(query) == 0:  
        messages.info(request, '  You search nothing THANKYOU.')           
        allPostst =  Post.objects.filter(title__icontains=query) 
        allPostsAdd = Post.objects.filter(content__icontains=query)
        allPosts =  allPostst.union(allPostsAdd)        
        params = {'allPosts': allPosts,'query': query} 
        return render(request,'home/search1.html',params)
    if len(query) > 50:
         messages.error(request, '  Error you have Given  many inputs which is not Present .')  
 
    allPostst =  Post.objects.filter(title__icontains=query) 
    allPostsAdd = Post.objects.filter(content__icontains=query)
    allPosts =  allPostst.union(allPostsAdd)
    allPostsAdd1 = Post.objects.filter(author__icontains=query)
    allPost1 = allPosts.union(allPostsAdd1)
    params = {'allPosts': allPost1,'query': query} 
    return render(request,'home/search.html',params)

 #  Apis in django authentication 
def handlesignup(request):
    if request.method =='POST':        
        username = request.POST['Username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pwd = request.POST['pwd']
        cpwd = request.POST['cpwd']  
        if len(username) < 8:
            messages.error(request,"  Username is too short")
            return redirect('home')
        if not username.isalnum():
            messages.error(request,"  Username in Alphanumeric   only")
            return redirect('home')
        if len(pwd) < 5:
            messages.error(request," Password is too short")
            return redirect('home')   
        if pwd != cpwd:  
            messages.error(request,"  Confirm Password did not match")
            return redirect('home')   
        myuser = User.objects.create_user(username, email, pwd)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"Your regestration sucessfully")
        return redirect('/')
    else:
        return HttpResponse("404-not found")

def handlelogin(request):
    if request.method =='POST':      
        username = request.POST['username']
        pwd1 = request.POST['pwd1']        
        user = authenticate(username=username, password = pwd1)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request,"Sucessfully login")
            return redirect('home')
        else:
            messages.info(request,"Invalid Credentials, Please try again !!!")
            return redirect('home')
    return HttpResponse('404-not found')

def handlelogout(request):
    logout(request)    
    messages.info(request,"Logout sucessfully !!!")  
    return redirect('home')  
    


         

        