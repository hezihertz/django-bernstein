from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('people.views',
	url(r'^$', 'list_current_members', name='list_current_members'),
	url(r'^current/$', 'list_current_members', name='list_current_members'),
	url(r'^former/$', 'list_former_members', name='list_former_members'),
)
