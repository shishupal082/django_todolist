# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
    
def anurag(request):
    return HttpResponse("Anurag Jain")
    
def results(request, todolist_id):
    return HttpResponse("results %s." % todolist_id)

def detail(request, todolist_id):
    return HttpResponse("You're looking at todolist detail %s." % todolist_id)
    
    #********************Project Start******************************************
    
def index(request):
    return render_to_response('index.html')
    
def collaborator(request):
    return render_to_response('collaborator.html')
    
def task(request):
    return render_to_response('task.html')
