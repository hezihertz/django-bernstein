from django.shortcuts import render_to_response
from django.template import RequestContext
from resources.models import Collaborator, Funding

title = "Resources"
side_nav = [{"url": "/resources/collaborators/", "url_title": "Collaborators"},
			{"url": "/resources/funding/", "url_title": "Funding"}
			]

def list_collaborators(request):
	active_nav = "/resources/collaborators/"
	clbs = Collaborator.objects.all().order_by('-list_order')
	return render_to_response('resources/collaborators.html', {
		'collaborators': clbs,
		'title': title,
		'side_nav': side_nav,
		'active_nav': active_nav
		}, context_instance = RequestContext(request))

def list_funding(request):
	active_nav = "/resources/funding/"
	funding = Funding.objects.all().order_by('-list_order')
	return render_to_response('resources/funding.html', {
		'funding': funding,
		'title': title,
		'side_nav': side_nav,
		'active_nav': active_nav
		}, context_instance = RequestContext(request))

