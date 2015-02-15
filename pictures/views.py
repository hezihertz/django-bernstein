from django.shortcuts import render_to_response
from django.template import RequestContext
from pictures.models import GroupPhoto, Poster

title = "Pictures"
side_nav = [{"url": "/pictures/group/", "url_title": "Group Photos"},
			{"url": "/pictures/posters/", "url_title": "Posters"}
			]

def list_group_photos(request):
	active_nav = "/pictures/group/"
	group_photos = GroupPhoto.objects.all().order_by('-list_order')
	return render_to_response("pictures/group_photos.html", {
		'group_photos': group_photos,
		'title': title,
		'side_nav': side_nav,
		'active_nav': active_nav
		}, context_instance=RequestContext(request))

def list_posters(request):
	active_nav = "/pictures/posters/"
	posters = Poster.objects.all().order_by('-list_order')
	return render_to_response("pictures/posters.html", {
		'posters': posters,
		'title': title,
		'side_nav': side_nav,
		'active_nav': active_nav
		}, context_instance=RequestContext(request))

