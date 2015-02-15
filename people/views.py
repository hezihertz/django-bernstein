from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from people.models import CurrentMember, FormerMember

title = "People"
side_nav = [{"url": "/people/current/", "url_title": "Group Members"},
			{"url": "/people/former/", "url_title": "Former Members"}
			]

def list_current_members(request):
	active_nav = "/people/current/"
	current_members = CurrentMember.objects.all().order_by('last_name')
	group_members = []

	grad_students = current_members.filter(work_title='GS')
	postdocs = current_members.filter(work_title='PF')
	undergrads = current_members.filter(work_title='US')
	visiting_scholars = current_members.filter(work_title='VS')
	research_scientists = current_members.filter(work_title='RS')
	lab_managers = current_members.filter(work_title='LM')
	technicians = current_members.filter(work_title='T')
	summer_students = current_members.filter(work_title='SS')
	lab_assistants = current_members.filter(work_title='LA')

	if lab_managers:
		group_members.append({'title': 'Laboratory Manager', 'members': lab_managers})
	if research_scientists:
		group_members.append({'title': 'Research Scientists', 'members': research_scientists})
	if postdocs:
		group_members.append({'title': 'Postdoctoral Fellows', 'members': postdocs})
	if grad_students:
		group_members.append({'title': 'Graduate Students', 'members': grad_students})
	if undergrads:
		group_members.append({'title': 'Undergraduate Students', 'members': undergrads})
	if visiting_scholars:
		group_members.append({'title': 'Visiting Scholars', 'members': visiting_scholars})
	if technicians:
		group_members.append({'title': 'Technicians', 'members': technicians})
	if summer_students:
		group_members.append({'title': 'Summer Students', 'members': summer_students})
	if lab_assistants:
		group_members.append({'title': 'Lab Assistants', 'members': lab_assistants})

	return render_to_response("people/current_members.html", {
		"title": title,
		"active_nav": active_nav,
		"side_nav": side_nav,
		"group_members": group_members
		}, context_instance=RequestContext(request))

def list_former_members(request):
	active_nav = "/people/former/"
	former_members = FormerMember.objects.all().order_by('last_name')
	return render_to_response("people/former_members.html", {
		'grad_students' : former_members.filter(work_title='GS'), 
		'postdocs' : former_members.filter(work_title='PF'), 
		'undergrads' : former_members.filter(work_title='US'), 
		'visiting_scholars' : former_members.filter(work_title='VS'), 
		'research_assistants' : former_members.filter(work_title='RA'), 
		"title": title,
		"active_nav": active_nav,
		"side_nav": side_nav
		}, context_instance=RequestContext(request))

