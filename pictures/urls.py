from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('pictures.views',
	url(r'^$', 'list_group_photos', name='list_group_photos'),
	url(r'^group/$', 'list_group_photos', name='list_group_photos'),
	url(r'^posters/$', 'list_posters', name='list_posters'),
)
