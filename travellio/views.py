from django.shortcuts import render
from .models import Destination
from .models import subs
def index(request):
	dests =Destination.objects.all()
	if request.method=="POST":
		if request.POST.get('name') and request.POST.get('email'):
			saver=subs()
			saver.name=request.POST.get('name')
			saver.email=request.POST.get('email')
			saver.save()
		return render(request,"index.html")
	return render(request,"index.html",{'dests':dests})
def about(request):
	return render(request,'about.html')
def register(request):
	dests =Destination.objects.all()
	return render(request,'register.html',{'dests':dests})
def BALI(request):
	return render(request,'bali.html')
def GREECE(request):
	return render(request,'Italy.html')
def MALDVIES(request):
	return render(request,'maldvies.html')