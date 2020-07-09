from django.urls import path

from . import views

urlpatterns = [
     path('',views.home,name='home'),
    path('image',views.image,name='image'),
    path('instance',views.instance,name='instance'),
    path('horizo',views.horizon,name='horizon'),
    path('volume',views.volume,name='volume'),
    path('network',views.network,name='network'),
    path('logout',views.logout,name='logout'),
    path('horizon_result',views.horizon_result,name='horizon_result'),   
    path('refresh_data',views.refresh_data,name='refresh_data'),
    path('neutron_result',views.neutron_result,name='neutron_result'),
]