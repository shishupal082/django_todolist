from django.conf.urls import patterns, url
from todolist import views
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    
    url(r'^collaborator$', views.collaborator, name='collaborator'), 
    
    url(r'^task$', views.task, name='task'),
    
    #url(r'^$', views.mystyle, name='bootstrap'),
    
    url(r'^anurag/$', views.anurag, name='anurag'),
    
    url(r'^results/(\d+)/$', views.results, name='results'),
   
)


urlpatterns += patterns('', (
    r'^(?P<path>.*)$','django.views.static.serve',{'document_root': settings.STATIC_ROOT}
))
