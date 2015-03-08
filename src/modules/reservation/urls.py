from django.conf.urls import patterns, url

from modules.reservation import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
