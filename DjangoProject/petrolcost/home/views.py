from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import Http404

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about-us.html')
