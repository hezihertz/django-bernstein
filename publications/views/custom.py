from django.shortcuts import render_to_response
from django.template import RequestContext
from publications.models import Publication

subfields = {'single_cell_genomics': 'Singel Cell Genomics',
			'single_molecule_enzymology': 'Single Molecule Enzymology',
			'single_molecule_spectroscopy': 'Single Molecule Spectroscopy',
			'gene_expression_in_living_cells': 'Gene Expression in Living Cells',
			'crs_microscopy': 'CRS Microscopy',
}

title = "Publications"
side_nav = [{"url": "/publications/year/", "url_title": "By Year"},
			{"url": "/publications/field/", "url_title": "By Field"}
			]


def category(request, category=None):
	active_nav = '/publications/field/'
	if category:
		publications = Publication.objects.filter(category = category).order_by("-category", "-year")
	else:
		publications = Publication.objects.exclude(category__isnull=True).order_by("-category", "-year")
	categories = []
	for publication in publications:
		if not publication.category:
			continue
		if not categories or categories[-1][0] != publication.category:
			categories.append((publication.category, subfields[publication.category], []))
		categories[-1][2].append(publication)
	return render_to_response('publications/categories.html',{
		'title': title,
		'side_nav': side_nav,
		'active_nav': active_nav,
		'categories' : categories
		}, context_instance=RequestContext(request))

def year_before_2001(request):
	years=[]
	publications = Publication.objects.filter(year__lt=2001, external=False)
	publications = publications.order_by('-year', '-month', '-id')

	for publication in publications:
		if publication.type.hidden:
			continue
		if not years or (years[-1][0] != publication.year):
			years.append((publication.year, []))
		years[-1][1].append(publication)

	if 'ascii' in request.GET:
		return render_to_response('publications/publications.txt', {
				'publications': sum([y[1] for y in years], [])
			}, context_instance=RequestContext(request), content_type='text/plain; charset=UTF-8')

	elif 'bibtex' in request.GET:
		return render_to_response('publications/publications.bib', {
				'publications': sum([y[1] for y in years], [])
			}, context_instance=RequestContext(request), content_type='text/x-bibtex; charset=UTF-8')

	elif 'rss' in request.GET:
		return render_to_response('publications/publications.rss', {
				'url': 'http://' + request.META['HTTP_HOST'] + request.path,
				'publications': sum([y[1] for y in years], [])
			}, context_instance=RequestContext(request), content_type='application/rss+xml; charset=UTF-8')

	else:
		for publication in publications:
			publication.links = publication.customlink_set.all()
			publication.files = publication.customfile_set.all()

		return render_to_response('publications/years.html', {
				'years': years
			}, context_instance=RequestContext(request))

def saar_science_2010_supp(request):
	return render_to_response('publications/saar_science_2010_supp.html',{
		'title': title,
		'side_nav': side_nav,
		}, context_instance=RequestContext(request))
