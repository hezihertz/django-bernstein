from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('news.views',
	url(r'^$', 'news_reports', name='news_reports'),
	url(r'^news_reports/$', 'news_reports', name='news_reports'),
	url(r'^group_news/$', 'group_news', name='group_news'),
	url(r'^archives/$', 'archives', name='archives'),
)
