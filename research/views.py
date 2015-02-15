from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import Http404

title = "Research"
side_nav = [{"url": "/research/overview/", "url_title": "Overview"},
			{"url": "/research/single_molecule_enzymology/", "url_title": "Single Molecule Enzymology"},
			{"url": "/research/single_molecule_spectroscopy/", "url_title": "Single Molecule Spectroscopy"},
			{"url": "/research/gene_expression_in_living_cells/", "url_title": "Gene Expression in Living Cells"},
			{"url": "/research/crs_microscopy/", "url_title": "CRS Microscopy"},
			{"url": "/research/single_cell_genomics/", "url_title": "Single Cell Genomics"} 
			]

def view(request, subfield="overview"):
	active_nav = "/research/" + subfield + "/"
	template_url = "research/" + subfield + ".html"
	if subfield not in ["overview", "single_molecule_enzymology", "single_molecule_spectroscopy", "gene_expression_in_living_cells", "crs_microscopy", "single_cell_genomics"]:
		raise Http404
	return render_to_response(template_url, {
		"title" : title,
		"side_nav": side_nav,
		"active_nav": active_nav
	}, context_instance = RequestContext(request))
	
	
