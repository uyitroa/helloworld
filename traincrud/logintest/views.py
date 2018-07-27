from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .custommodels import Account

# Create your views here.
def log_in(request):
	username = request.POST['username']
	password = request.POST['password']

	a = Account()
	acc = a.read(username, password)

	if acc != None:
		return HttpResponse(acc['info'])
	else:
		return HttpResponseRedirect('')

def home(request):
	return render(request, 'home.html')

def createPage(request):
	return render(request, 'register.html')

def createAcc(request):
	username = request.POST['username']
	password = request.POST['password']
	info = request.POST['info']

	a = Account()
	a.create(username, password, info)
	return HttpResponseRedirect('')
