# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response

def contact(request):
	title = "Contact"
	return render_to_response("contact/contact.html", {"title": title}, context_instance = RequestContext(request))
