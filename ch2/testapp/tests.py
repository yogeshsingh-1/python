from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def greetings(request):
    S = "<h3>Welcome in our website</h3>"
    return HttpResponse(S)

def about(request):
    S = "<h4>This is a about Page</h4>"
    return HttpResponse(S)

def contact(request):
    S = "<h5>This is Http contact Page</h5>"
    return HttpResponse(S)
