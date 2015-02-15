from django.conf.urls.defaults import patterns, url
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

urlpatterns = patterns('about_xie.views',
	url(r'^$', 'overview', name='overview'),
	url(r'^overview/$', 'overview', name='overview'),
	url(r'^bio/$', 'bio', name='bio'),
	url(r'^key_pub_list/$', 'featured', name='featured'),
	url(r'^full_pub_list/$', 'full', name='full'),
	url(r'^review/$', 'review', name='review'),
)
