from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('contact.views',
	url(r'^$', 'contact', name='contact'),
)
