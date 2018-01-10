from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string
# Create your views here.
def index(request):
	if 'counter' in request.session:
		request.session['counter'] += 1
	else:
		request.session['counter'] = 1
	content = {
		"random_word": get_random_string(length=14),
	}
	return render(request, "random_word_generator/index.html", content)

def generate(request):
	if request.method == "POST":
		print request.POST['button']
	return redirect('/')