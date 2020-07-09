from django.shortcuts import render
from django.http import HttpResponse  
from . models import neutron_log,horizon_log
import datetime
from datetime import datetime
from django.db.models import Q

import json 
from bson import json_util
from django.http import JsonResponse
from django.core import serializers
import logging

# Create your views here.
def home(request):
    return render(request,'home.html')

def horizon(request):
    count=horizon_log.objects.all().count()
    count_get=horizon_log.objects.filter(method="GET").count()
    count_post=horizon_log.objects.filter(method="POST").count()
    count_200=horizon_log.objects.filter(apache_status=200).count()
    count_201=horizon_log.objects.filter(apache_status=201).count()
    return render(request,'horizon.html',{"count":count,"count_get":count_get,"count_post":count_post,"count_200":count_200,"count_201":count_201})

def image(request):
    return render(request,'image.html')

def instance(request):
    return render(request,'instance.html')

def network(request):
    count=neutron_log.objects.all().count()
    count_info=neutron_log.objects.filter(priority="INFO").count()
    count_debug=neutron_log.objects.filter(priority="DEBUG").count()
    count_audit=neutron_log.objects.filter(priority="AUDIT").count()
    count_warning=neutron_log.objects.filter(priority="WARNING").count()
    count_error=neutron_log.objects.filter(priority="ERROR").count()
    
    count_server=neutron_log.objects.filter(agent_name="neutron-server[13776]").count()
    count_dhcp=neutron_log.objects.filter(agent_name="neutron-dhcp-agent[16323]").count()
    count_l3=neutron_log.objects.filter(agent_name="neutron-l3-agent[17023]").count()
    count_openvswitch=neutron_log.objects.filter(agent_name="neutron-openvswitch-agent[15619]").count()
    return render(request,'network.html',{"count":count,"count_info":count_info,"count_debug":count_debug
    ,"count_audit":count_audit,"count_warning":count_warning,"count_error":count_error,"count_server":count_server,"count_dhcp":count_dhcp,"count_l3":count_l3,"count_openvswitch":count_openvswitch})
    




def neutron_result(request):
    # count=neutron_log.objects.all().count()
    from_date= request.GET.get('FromDate')
    to_date=request.GET.get('ToDate')
    log_level=request.GET.get('priority') 
    neutron_agent=request.GET.get('neutron_agent')
    neutron_id=request.GET.get('network_id')
    log=neutron_log.objects.filter(Q(remaining_log__contains=neutron_id),date__range=[from_date, to_date])
    count=log.count()
    # log=neutron_log.objects.filter(date__range=[from_date, to_date],priority=log_level,agent_name=neutron_agent )
    return render(request, 'network_result.html',{"data":log,"count":count})


        




def volume(request):
    return render(request,'volume.html')

def logout(request):
    return render(request,'logout.html')

def horizon_result(request):
    # count=horizon_log.objects.all().count()
    from_date= request.GET.get('FromDate')
    to_date=request.GET.get('ToDate')
    # from_date=datetime.datetime.strptime(request.GET.get('FromDate'),"%Y-%m-%d").strftime('%b.%d %Y')
    # to_date= datetime.datetime.strptime(request.GET.get('ToDate'),"%Y-%m-%d").strftime('%b.%d %Y')
    method_type= request.GET.get('method')
    apache_code= request.GET.get('apache_status')
    if (method_type=="Select"):
        if apache_code != "":
            log=horizon_log.objects.filter(date__range=[from_date, to_date],apache_status=apache_code)
            count=log.count()
            if (count != 0):
                return render(request, 'horizon_result.html',{"data":log,"count":count})
            else:
                return render(request, 'Null_horizon_op.html')
        else:
            log=horizon_log.objects.filter(date__range=[from_date, to_date])
            count=log.count()
            if (count != 0):
                return render(request, 'horizon_result.html',{"data":log,"count":count})
            else:
                return render(request, 'Null_horizon_op.html')
    if method_type in ('GET', 'POST'):
        if apache_code != "":  
            log=horizon_log.objects.filter(date__range=[from_date, to_date],method=method_type,apache_status=apache_code)
            count=log.count()
            if (count != 0 ):
                return render(request, 'horizon_result.html',{"data":log,"count":count})
            else:
                return render(request, 'Null_horizon_op.html')
        else:
            log=horizon_log.objects.filter(date__range=[from_date, to_date],method=method_type)
            count=log.count()
            if (count != 0):
                return render(request, 'horizon_result.html',{"data":log,"count":count})
            else:
                return render(request, 'Null_horizon_op.html')
    # return HttpResponse(count)








# #output unformatted data
# def horizon_date(request):    
#     log_list=list(horizon_log.objects.all())
#     log_json = serializers.serialize("json",log_list)
#     log_obj = json.loads(log_json)
#     logs=[]
#     logs=logs.append(json.dumps( log_obj))
#     # return HttpResponse(json.dumps( log_obj),content_type="application/json")
#     return render(request, 'horizon_date.html',logs,content_type="application/json")
    

    
    


def refresh_data(request):
    try:
        with open('logFind/horizon_data.txt') as json_file1:
            data1 = json.load(json_file1)
        for i in data1:
            x = datetime.strptime(i['date'],"%d/%b/%Y")
            horizon_log.objects.create(id=i['id'],remote_host=i['remote_host'],date =x,time = i['time'],zone=i['zone'],method=i['method'],browser_path=i['browser_path'],apache_status=i['apache_status'],data_transfer=i['data_transfer'],message=i['message'])

        # with open('logFind/neutron_data.txt') as json_file2:
        #     data2 = json.load(json_file2)
        # for i in data2:
        #     x = datetime.strptime(i['date'],"%b %d %Y")
        #     neutron_log.objects.create(id=i['id'],date =x,time = i['time'],host_name=i['host_name'],agent_name=i['agent_name'],priority=i['priority'],agent_details=i['agent_details'],request_details=i['request_details'],remaining_log=i['remaining_log'])
    except Exception as e:
        return HttpResponse(e)
    return HttpResponse("Successfully loaded data")

