from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from libapp.models import Book

# Create your views here.
def home(request):
    return render(request,'home.html')

def admin_signup(request):
    if request.method=="POST":
        fm=UserCreationForm(request.POST)
        print(fm)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password1']
            #print(uname)
            #print(upass)
            u=User.objects.create_user(username=uname,password=upass,is_superuser=True,is_staff=True)
            u.save()
            return HttpResponseRedirect('/user_login')
            
    else:
        fm=UserCreationForm()
    return render(request,'admin_signup.html',{'form':fm})

def signup(request):
    if request.method=="POST":
        fm=UserCreationForm(request.POST)
        #print(fm)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password1']
            #print(uname)
            #print(upass)
            u=User.objects.create_user(username=uname,password=upass,is_staff=True)
            u.save()
            return HttpResponseRedirect('/user_login')
            
    else:
        fm=UserCreationForm()
    return render(request,'signup.html',{'form':fm})
    

def user_login(request):
    if request.method=="POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        #print(fm)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            #print(uname)
            #print(upass)
            u=authenticate(username=uname,password=upass)
            if u is not None:
                #print("valid user")
                login(request,u)
                return HttpResponseRedirect('/dashboard')
    else:
        fm=AuthenticationForm()

    return render(request,'user_login.html',{'form':fm})

def user_logout(request):
     logout(request)
     return HttpResponseRedirect('/')

def dashboard(request):

    #collecting authenticated user id from the session
    c=request.user
    cuid=c.id
    #print(cuid)
    u=User.objects.get(id=cuid)
    #print(u.is_superuser)
    b=Book.objects.all()
    content={}
    content['data']=b
    content['is_superuser']=u.is_superuser
    return render(request,'dashboard.html',content)

def add_book(request):
    if request.method=="POST":
        bname=request.POST['bname']
        bauthor=request.POST['bauthor']
        #print(bname)
        # print(bauthor)
        b=Book.objects.create(book_name=bname,book_author=bauthor)
        b.save()
        return HttpResponseRedirect('/dashboard')

    else:
        return render(request,'add_book.html')

def delete_book(request,rid):
    b=Book.objects.filter(id=rid)
    b.delete()
    return HttpResponseRedirect('/dashboard/')

def edit_book(request,rid):
    if request.method=="POST":
        #print(rid)
        ubname=request.POST['bname']
        uauthor=request.POST['bauthor']
        b=Book.objects.filter(id=rid)
        b.update(book_name=ubname,book_author=uauthor)
        return HttpResponseRedirect('/dashboard/')

    else:
        b=Book.objects.filter(id=rid)
        content={}
        content['data']=b
        return render(request, 'edit_book.html',content)