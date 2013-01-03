from django.db import models

# Create your models here.

class Projects(models.Model) :
    project_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.project_name
    
    def was_published_recently(self):
        return self.project_name >= timezone.now() - datetime.timedelta(days=1)
        
    was_published_recently.admin_order_field = 'project_name'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Collaborator(models.Model):
    project = models.ForeignKey(Projects)
    collaborator_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.collaborator_name
        
    def was_published_recently(self):
        return self.collaborator_name >= timezone.now() - datetime.timedelta(days=1)
        
    was_published_recently.admin_order_field = 'collaborator_name'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    

class Task(models.Model):
    collaborator = models.ForeignKey(Collaborator)
    task_name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.task_name
    def was_published_recently(self):
        return self.task_name >= timezone.now() - datetime.timedelta(days=1)
        
    was_published_recently.admin_order_field = 'task_name'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
