from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	url(r'^$', 'home.views.home'),
	url(r'^people/', include('people.urls')),
	url(r'^pictures/', include('pictures.urls')),
	url(r'^resources/', include('resources.urls')),
	url(r'^publications/', include('publications.urls')),
	url(r'^news/', include('news.urls')),
	url(r'^about_xie/', include('about_xie.urls')),
	url(r'^research/', include('research.urls')),
	url(r'^contact/', include('contact.urls')),
	url(r'^intranet/', include('intranet.urls')),
	url(r'^admin/publications/publication/import_bibtex/$', 'publications.admin_views.import_bibtex'),
    # Uncomment the admin/doc line below to enable admin documentation:
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)		#NOTE: THIS LAST LINE ONLY WORKS IN DEVELOPMENTAL STAGE
