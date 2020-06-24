from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.models import User
from .models import Messages
from .forms import UserForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

class Index(TemplateView):
    template_name = 'index.html'

def messages(request,pk):
    user= User.objects.filter(pk=pk)
    usermessages = user[0].received_messages.all().order_by('-sent_date')
    return render(request,'Messages.html',{'messages':usermessages})

def sendmessage(request):
    if request.method=='POST':
        sender=request.POST['sender']
        text = request.POST['text']
        img = None
        mfile = None
        if 'image' in request.FILES:
            img = request.FILES['image']
        if 'file' in request.FILES:
            mfile = request.FILES['file']
        reciever = request.POST['receiver']
        user=User.objects.all().filter(username=reciever)
        sender = User.objects.all().filter(username=sender)
        message = Messages(sender=sender[0],text=text,receiver=user[0],MFile=mfile, MImage=img ,sent_date=timezone.now())
        message.save()
        return redirect('/')
    return render(request,'sendmessage.html')

class UserCreateView(CreateView):
    template_name = 'registration.html'
    form_class = UserForm
    model = User
    success_url = reverse_lazy('index')

def user_login(request):

    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST['password']
        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect('/')
            else:
                return HttpResponse('Account Not active')
        else:
            return HttpResponse('Invalid Credentials')
    else:
        return render(request,'login.html') 

@login_required
def user_logout(request):
    logout(request)
    return redirect('/')
    

