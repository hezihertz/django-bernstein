from django.conf.urls.defaults import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('intranet.views',
	url(r'^$', 'view'),
	url(r'^(?P<category>.+)/$', 'view'),
)
