from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from home.models import Hit

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_user_agent(request):
	user_agent = request.META['HTTP_USER_AGENT']
	if len(user_agent)>256:
		user_agent = user_agent[:256]
	return user_agent

def home(request):
	new_hit = Hit(ip_addr = get_client_ip(request), user_agent = get_user_agent(request))
	new_hit.save()
	return render_to_response("index.html", {"title" : "Home"}, context_instance = RequestContext(request))
