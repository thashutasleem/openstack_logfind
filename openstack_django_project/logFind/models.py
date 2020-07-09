# from django.db import models
import openstack_django_project.settings
from djongo import models

# Create your models here.

class horizon_log(models.Model):
    id= models.IntegerField(primary_key=True) 
    remote_host = models.TextField()
    date  = models.DateField()
    time = models.TimeField()
    zone= models.IntegerField()
    method=models.CharField(max_length = 100)
    browser_path= models.TextField()
    apache_status= models.IntegerField()
    data_transfer= models.IntegerField()
    message=models.TextField()
    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s %s'%(self.id,self.remote_host,self.date,self.time,self.zone,self.method,self.browser_path,self.apache_status,self.data_transfer,self.message)


class neutron_log(models.Model):
    id= models.IntegerField(primary_key=True)
    date  = models.DateField() 
    time = models.TimeField()
    host_name = models.TextField()
    agent_name= models.TextField()
    priority = models.TextField()
    agent_details= models.TextField()
    request_details= models.TextField()
    remaining_log=models.TextField()
    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s'%(self.id,self.date,self.time,self.host_name,self.agent_name,self.priority,self.agent_details,self.request_details,self.remaining_log)
