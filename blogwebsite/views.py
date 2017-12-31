# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'blogwebsite/home.html')
def contact(request):
	return render(request,'blogwebsite/basic.html')
def resume(request):
	return render(request,'blogwebsite/resume.html')