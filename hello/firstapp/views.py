from django.shortcuts import render
from firstapp.forms import*

# Create your views here.
def home(request):
	return render(request,'index.html')
def employee(request):
	if request.method=="POST":
		lf=LoginForm(request.POST)
		if lf.is_valid():
			try:
				If.save()
				return redirect('/')
			except:
				pass
	else:
		lf=LoginForm()
	return render(request,'emp.html',{'form':lf})
def show(request):
	return render(request,'display.html')
