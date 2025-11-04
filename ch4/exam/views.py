from django.shortcuts import render
from django.http import HttpResponse
 

def viewsIntemplate (request):
    s = "<h3>this is a view template in the views.py file</h3>"
    return HttpResponse(s)

def dynamicTemplate(request):
    return render(request,'emailtemplate.html')

def menu(request):
    obj = {
        "names" : ["hari","ram","ankur","shyam"],
        "email" :"dotnet@reply.com"
    }
    return render(request,'menu.html',obj)