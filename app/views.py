from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile, Picture, Usercap, Vote_Picture, Vote_Caption, Friendship #, Card
from .forms import LoginForm, SignUpForm
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
import requests
from rest_framework import viewsets
from .serializers import ProfileSerializer, PictureSerializer, UsercapSerializer, Vote_PictureSerializer, Vote_CaptionSerializer, FriendshipSerializer

class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class PictureView(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class UsercapView(viewsets.ModelViewSet):
    queryset = Usercap.objects.all()
    serializer_class = UsercapSerializer

class Vote_PictureView(viewsets.ModelViewSet):
    queryset = Vote_Picture.objects.all()
    serializer_class = Vote_PictureSerializer

class Vote_CaptionView(viewsets.ModelViewSet):
    queryset = Vote_Caption.objects.all()
    serializer_class = Vote_CaptionSerializer

class FriendshipView(viewsets.ModelViewSet):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer


# Create your views here.

def index(request):
    print('okay')
    return render(request, 'index.html')

def snaps(request):
    # if HttpRequest.GET:
    #     data = 
    # else:
    data = serializers.serialize("json", Picture.objects.all())
    return HttpResponse(data, content_type='application/json')

def details(request, snap_id):
    # Picture.objects.get(pk=toy_id)
    data = serializers.serialize("json", Picture.objects.get(pk=snap_id))
    return HttpResponse(data, content_type='application/json')

def friends(request):
    # Picture.objects.filter()
    data = { "test": "friends route"}
    return HttpResponse(data, content_type='application/json')

def category(request, category):
    # Picture.objects.filter()
    data = { "test": "category route"}
    return HttpResponse(data, content_type='application/json')

def snap_vote(request, snap_id):
    return HttpResponse("Snap vote recorded.")

def signup(request):
    return HttpResponse("User registered.")

def login(request):
    return HttpResponse("Login successful.")

def logout(request):
    return HttpResponse("Logout successful.")

def profile(request, profile_id):
    if request.method == "GET":
        data = { "test": "profile route"}
        return HttpResponse(data, content_type='application/json')
    if request.method == "PUT":
        return HttpResponse("Profile updated.")
    if request.method == "DELETE":
        return HttpResponse("Profile deleted.")

def cap_vote(request, cap_id, is_card):
    return HttpResponse("Snap vote recorded.")
