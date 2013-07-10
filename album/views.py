# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

from album.models import Image
from album.forms import ImageForm

#userlogin
def userlogin(request):
    if request.method=='GET':
        return render_to_response('home.html')
    if request.method=='POST':
        usrname=request.POST['username']
        passwrd=request.POST['password']
        user=authenticate(username=usrname,password=passwrd)
        if user is not None and user.is_active:
            login(request,user)
            return HttpResponseRedirect('/album/')
        else:
            return render_to_response('home.html',{'error_msg':"Invalid User!!"})

#register user
def register(request):
    if request.method=='GET':
        return render_to_response('register.html')
    if request.method=='POST':
        new_usrname=request.POST['username']
        new_email=request.POST['email']
        new_passwrd=request.POST['password']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        conf_password=request.POST['conf_password']
        if new_passwrd != conf_password:
            return render_to_response('register.html',{'error_msg':"Passwords Don't Match"})
        user=User.objects.create_user(username=new_usrname,email=new_email,password=new_passwrd)
        user.first_name=firstname
        user.last_name=lastname
        user.save()
        user=authenticate(username=new_usrname,password=new_passwrd)
        if user is not None and user.is_active:
            login(request,user)
            return HttpResponseRedirect('/album/')
        else:
            return HttpResponseRedirect('/')

#form
def img_list(request):
    usr=request.user
    if not usr.is_authenticated():
        raise PermissionDenied
    else:
        if request.method == 'POST':
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                newimg = Image(imgfile = request.FILES['imgfile'],username=usr.username)
                newimg.save()
                return HttpResponseRedirect('/album/')
        else:
            form = ImageForm()
            imgs = Image.objects.filter(username=usr.username)
            return render_to_response('list.html',{'images': imgs,'user':usr,'form': form},context_instance=RequestContext(request))

#logout
def usrlogout(request):
    logout(request)
    return HttpResponseRedirect("/")

