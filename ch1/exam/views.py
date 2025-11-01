from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def science(request):
    s ="<h5>THis is a science test exam.</h5>"
    return HttpResponse(s)

def math(request):
    s = "<h6>This is a math test exam</h6>"
    return HttpResponse(s)