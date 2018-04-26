from django.conf.urls import url
from mainapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'alarms/', views.alarms, name='alarms'),
    url(r'positions/', views.positions, name='positions'),
    url(r'params/', views.params, name='params'),
    url(r'cctv/', views.cctv, name='cctv'),
    url(r'curr_settings/', views.curr_settings, name='curr_settings'),
    url(r'changeable_settings/', views.changeable_settings, name='changeable_settings'),

]