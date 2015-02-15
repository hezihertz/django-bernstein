from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from news.models import NewsItem

title = "News"
side_nav = [{"url": "/news/news_reports/", "url_title": "News Reports"},
			{"url": "/news/group_news/", "url_title": "Group News"},
			{"url": "/news/archives/", "url_title": "Archives"}]

def news_reports(request):
	active_nav = "/news/news_reports/"
	news_items = NewsItem.objects.filter(category = 'NR').order_by('-year', '-month')
	return render_to_response("news/news.html", {
		"title" : title,
		"side_nav": side_nav,
		"active_nav": active_nav,
		"tag" : "news_reports",
		"news_items" : news_items,
	}, context_instance = RequestContext(request))

def group_news(request):
	active_nav = "/news/group_news/"
	news_items = NewsItem.objects.filter(category = 'GN').order_by('-year', '-month')
	return render_to_response("news/news.html", {
		"title" : title,
		"side_nav": side_nav,
		"active_nav": active_nav,
		"news_items" : news_items,
		"tag" : "group_news",
	}, context_instance = RequestContext(request))

def archives(request):
	active_nav = "/news/archives/"
	news_items = NewsItem.objects.filter(category = 'AR').order_by('-year', '-month')
	return render_to_response("news/news.html", {
		"title" : title,
		"side_nav": side_nav,
		"active_nav": active_nav,
		"news_items" : news_items,
		"tag" : "archives",
	}, context_instance = RequestContext(request))
