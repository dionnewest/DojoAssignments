from django.shortcuts import render, HttpResponse, redirect

#urls for BLOG app

def index(request):
	return render(request, "blogs/index.html")