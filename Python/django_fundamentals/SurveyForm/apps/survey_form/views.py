from django.shortcuts import render, HttpResponse, redirect

def index(request):
	return render(request, "survey_form/index.html")

def result(request):
	if 'count' in request.session:
		request.session['count'] += 1
	else:
		request.session['count'] = 1
	request.session['name'] = request.POST['name']
	request.session['location'] = request.POST['location']
	request.session['language'] = request.POST['language']
	request.session['comment'] = request.POST['comment']
	return render(request, "survey_form/result.html")
	
def goback(request):
	return redirect('/')
