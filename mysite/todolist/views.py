# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html')
    
def anurag(request):
    return HttpResponse("Anurag Jain")
    
def results(request, todolist_id):
    return HttpResponse("index Three %s." % todolist_id)

def collaborator(request):
    return render_to_response('collaborator.html')
    
def task(request):
    return render_to_response('task.html')