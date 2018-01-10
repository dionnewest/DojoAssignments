from django.shortcuts import render

#urls for SURVEY app

def index(request):
	return render(request, "surveys/index.html")