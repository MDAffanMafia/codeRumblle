# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.conf import settings
from models import User,Questions2
from django.contrib.auth import authenticate
from django.urls import reverse

# Create your views here.
save=""
def leaderboard(request):
    if 'login_status' in request.COOKIES:
        
        
        user=Questions2.objects.all()
        print("that is the on e")
        return render(request,'leaderboard.html',{'user_dis':user})
    else:
        return  render(request,'login.html')
def login(request):
  if request.method=='POST':
     username=request.POST['username']
     password=request.POST['password']
     allUser=User.objects.all()
     h=False
     b="yes"
     for user in allUser:
        if user.username==username:
            if user.password==password:
                print("got it")
                #cassandra_session.save()
                response=render(request,'leaderboard.html')
                response.set_cookie('login_status',True)
                save=username
                h=True
                break
     if h==True:
         h=False
         return redirect(reverse(leaderboard))
     else:
         return redirect(r'^login/')   
  return render(request,'login.html')
def register(request):
  if request.method=='POST':
     username=request.POST['username']
     password=request.POST['password']   
     wins=0
     matches=0
     rank=0
     new_user=User( username=username,password=password,wins=wins,matches=matches,rank=rank)
     new_user.save()
     b="yes"
  return render(request,'register.html')
def profile(request):
    return render(request,'profile.html')
def compete(request):
    if request.method=='POST':
        question_name=request.POST['name']
        link=request.POST['link']
        difficulty=request.POST['difficulty']
        question=Questions2(question_name=question_name,link=link,difficulty=difficulty)
        question.save()
    return render(request,'compete.html')
def log(request):
    
    return render(request,'logout.html')