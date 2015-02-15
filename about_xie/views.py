from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from about_xie.models import Background, BackgroundForm
from publications.models import Publication

title = "Prof. Xie"
side_nav = [{"url": "/about_xie/overview/", "url_title": "Overview"},
			{"url": "/about_xie/bio/", "url_title": "Xie Bio"},
			{"url": "/about_xie/key_pub_list/", "url_title": "Key Publication List"},
			{"url": "/about_xie/full_pub_list/", "url_title": "Full Publication List"},
			{"url": "/about_xie/review/", "url_title": "Review Articles"},
			{"url": "/media/news/xie_pioneer_2009.pdf", "url_title": "Article By Barbara Goode"},
			{"url": "/media/news/BTN_A_000114153_O_232274a-2.pdf", "url_title": "Interview with Kirstie Kybo"} 
			]

subfields = {'single_cell_genomics': 'Singel Cell Genomics',
			'single_molecule_enzymology': 'Single Molecule Enzymology',
			'single_molecule_spectroscopy': 'Single Molecule Spectroscopy',
			'gene_expression_in_living_cells': 'Gene Expression in Living Cells',
			'crs_microscopy': 'CRS Microscopy',
}

def overview(request):
	educations = Background.objects.filter(category="Education").order_by('-year_start')
	appointments = Background.objects.filter(category="Appointments").order_by('-year_start')
	honors = Background.objects.filter(category="Honors").order_by('-year_start')
	lectureships = Background.objects.filter(category="Lectureships").order_by('-year_start')
	interests = Background.objects.filter(category="Interests").order_by('-year_start')
	active_nav = "/about_xie/overview/"
	return render_to_response("about_xie/overview.html", {
		'educations' : educations, 
		'appointments' : appointments, 
		'honors' : honors, 
		'lectureships' : lectureships, 
		'interests' : interests, 
		"title" : title,
		"side_nav": side_nav,
		"active_nav": active_nav
		}, context_instance=RequestContext(request))

def bio(request):
	active_nav = "/about_xie/bio/"
	return render_to_response("about_xie/xie_bio.html", {
		"title" : title,
		"side_nav": side_nav,
		"active_nav": active_nav
		}, context_instance=RequestContext(request))

def full(request):
	active_nav = "/about_xie/full_pub_list/"
	publications = Publication.objects.all()	#filter the ones with "xie"
	return render_to_response('publications/xie_full.html',{
		"title" : title,
		"side_nav": side_nav,
		"active_nav": active_nav,
		'publications' : publications
		}, context_instance=RequestContext(request))

def featured(request):
	active_nav = "/about_xie/key_pub_list/"
	all_pub = Publication.objects.filter(featured = True)
	publications = []
	for key, value in subfields.items():
		current_pub = all_pub.filter(category=key)
		publications.append({'title': value, 'pub_list': current_pub})
	return render_to_response('publications/xie_key.html',{
		"title" : title,
		"side_nav": side_nav,
		"active_nav": active_nav,
		'publications' : publications
		}, context_instance=RequestContext(request))

def review(request):
	active_nav = "/about_xie/review/"
	publications = Publication.objects.filter(review = True)
	return render_to_response('publications/xie_review.html',{
		"title" : title,
		"side_nav": side_nav,
		"active_nav": active_nav,
		'publications' : publications
		}, context_instance=RequestContext(request))
