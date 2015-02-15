from django.conf.urls.defaults import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('resources.views',
	url(r'^$', 'list_collaborators', name='list_collaborators'),
	url(r'^collaborators/$', 'list_collaborators', name='list_collaborators'),
	url(r'^funding/$', 'list_funding', name='list_funding_sources'),
)
