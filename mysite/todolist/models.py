from django.db import models

# Create your models here.

class Projects(models.Model) :
    project_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.project_name
    
class Collaborator(models.Model):
    project = models.ForeignKey(Projects)
    collaborator_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.collaborator_name
        
class Task(models.Model):
    collaborator = models.ForeignKey(Collaborator)
    task_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.task_name
