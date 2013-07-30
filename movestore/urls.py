from django.conf.urls import patterns, url

from movestore import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<move_id>\d+)/(?P<vocabpair_id>\d+)/$', views.move, name='move'),
)
