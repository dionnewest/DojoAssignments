from django.shortcuts import render, redirect,HttpResponse
from .models import *
# from apps.book_app.models import *
# # Create your views here.

def index(req):

    return render(req, 'login_reg/index.html')

def login(req):
    result = User.manager.login(req.POST)
    if result[0]:
        req.session['user_id'] = result[1].id
        print "#"*20
        print req.session['user_id']
        print "#"*20
        return redirect('/books')
    for key, message in result[1].iteritems():
        messages.error(req, message)
    return redirect('/')

def createUser(req):
    result = User.manager.createUser(req.POST)
    if not result[0]:
        for key, message in result[1].iteritems():
            messages.error(req, message)
    return redirect('/')

def user(req, id):
    user = User.manager.get(id=id)
    user_books = user.books.all()
    context = {
        'user': user,
        'books': user_books
    }
    return render(req, '/login_reg/profile.html', context)

def logout(req):
    req.session.clear()
    return redirect('/')
