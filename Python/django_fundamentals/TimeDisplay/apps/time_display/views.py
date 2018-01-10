from django.shortcuts import render, HttpResponse, redirect
from time import strftime, localtime

# Create your views here.
def index(request):
	context = {
	"date":strftime("%B %m, %Y", localtime()),
	"time":strftime("%I:%M %p"),
	}
	return redirect(request,'time_display/index.html', context)