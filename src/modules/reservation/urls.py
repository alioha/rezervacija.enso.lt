from django.conf.urls import patterns, url

from modules.reservation import views

urlpatterns = patterns('',
    url(r'^$', views.events, name='events'),
    url(r'^account/create$', views.account_create, name='account_create'),
    url(r'^account/login$', views.account_login, name='account_login'),
    url(r'^account/logout$', views.account_logout, name='account_logout'),
)
