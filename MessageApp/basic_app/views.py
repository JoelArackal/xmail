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
from django.views.decorators.csrf import csrf_exempt
import socket

from .serializers import MessageSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

import smtplib
from email.mime.text import MIMEText



# Create your views here.
'''
s = socket.socket()
s.bind(('192.168.56.1',1024))
'''
class Index(TemplateView):
    template_name = 'index.html'

@login_required
def messages(request,pk):
    user= User.objects.filter(pk=pk)
    usermessages = []
    if request.user == user[0]:
        usermessages = user[0].received_messages.all().order_by('-sent_date')
    return render(request,'Messages.html',{'messages':usermessages})

@login_required
def sendmessage(request):
    if request.method=='POST':
        sender=request.POST['sender']
        sender = request.user
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
        body = "This is a test email."

        msg = MIMEText(body)
        msg['From'] = 'joeljosearackal@gmail.com'
        msg['To'] = 'joel_b170223ec@nitc.ac.in'
        msg['Subject'] = 'Testing'

        server = smtplib.SMTP('smtp.gmail.com',587)

        server.starttls()

        server.login('joeljosearackal@gmail.com','9495748107')
        server.send_message(msg)

        print('Mail Sent')

        server.quit()
        return redirect('/')
    return render(request,'sendmessage.html')

class UserCreateView(CreateView):
    template_name = 'registration.html'
    form_class = UserForm
    model = User
    success_url = reverse_lazy('index')

# @csrf_exempt
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


class MessageApi(APIView):
    def get(self,request):
        MessageX = Messages.objects.all()
        serializer = MessageSerializer(MessageX,many=True)
        return Response(serializer.data)
    

