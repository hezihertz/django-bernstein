from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from people.models import CurrentMember
from django.http import Http404
from lockdown.decorators import lockdown
from lockdown.forms import AuthForm

title = "Intranet"
side_nav = [{"url": "/intranet/contact_list/", "url_title": "Contact List"},
			{"url": "/intranet/departure_check_list/", "url_title": "Departure Check List"},
			{"url": "/intranet/equipment_responsibility_list/", "url_title": "Equipment Responsibility List"},
			{"url": "/intranet/printer_setup/", "url_title": "Adding Group Printers"},
			{"url": "/intranet/odyssey_faq/", "url_title": "Odyssey FAQ"},
			{"url": "/media/intranet/objective_inventory.xls", "url_title": "Objective Inventory"},
			{"url": "/media/intranet/Xie_Group_Bacterial_Strain_Stock_Database.xls", "url_title": "Baterial Strain Stock Database"},
			]

@lockdown(form = AuthForm, staff_only=False)
def view(request, category="contact_list"):
	if category=="contact_list":
		current_members = CurrentMember.objects.all().order_by('last_name')
	else:
		current_members = ""
	active_nav = "/intranet/" + category + "/"
	template_url = "intranet/" + category + ".html"
	if category not in ["contact_list", "departure_check_list", "equipment_responsibility_list", "printer_setup", "odyssey_faq"]:
		raise Http404
	return render_to_response(template_url, {
		"title" : title,
		"side_nav": side_nav,
		"active_nav": active_nav,
		'current_members' : current_members
	}, context_instance = RequestContext(request))
	
