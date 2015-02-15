__license__ = 'MIT License <http://www.opensource.org/licenses/mit-license.php>'
__author__ = 'Lucas Theis <lucas@theis.io>'
__docformat__ = 'epytext'

try:
	from django.conf.urls import patterns
except ImportError:
	from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
	(r'^$', 'publications.views.year'),
	(r'^year/$', 'publications.views.year'),
	(r'^year/before_2001/$', 'publications.views.custom.year_before_2001'),
	(r'^year/(?P<year>\d+)/$', 'publications.views.year'),
	(r'^tag/(?P<keyword>.+)/$', 'publications.views.keyword'),
	(r'^list/(?P<list>.+)/$', 'publications.views.list'),
	(r'^field/$', 'publications.views.custom.category'),
	(r'^field/(?P<category>.+)/$', 'publications.views.custom.category'),
	(r'^saar_science_2010_supp/$', 'publications.views.custom.saar_science_2010_supp'),
)
