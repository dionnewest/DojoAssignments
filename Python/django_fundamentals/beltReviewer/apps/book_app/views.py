from django.shortcuts import render

from ..login_reg.models import *
from .models import *

# Create your views here.
def index(req):
    return render(req,'book_app/index.html')
def addBook(req):
	context = {
		'books':Book.objects.all().order_by('author'),
	}
	return render(req,'book_app/create_book.html', context)

def createBook(req):

    return redirect('books/{}'.format(id))

def details(req):
	context = {
		'user':User.manager.get(id=req.session['user_id']),
		'reviews':Review.objects.all().order_by('-id')[:3],
		'book_list':Book.objects.all().order_by('title')
	}
	
	return render(req,'book_app/details.html', context)
