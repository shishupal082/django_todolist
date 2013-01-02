from django.contrib import admin
#these are the classes that defines in model
from todolist.models import Projects
from todolist.models import Collaborator
from todolist.models import Task

admin.site.register(Projects)
admin.site.register(Collaborator)
admin.site.register(Task)
