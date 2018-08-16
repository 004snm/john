from django.shortcuts import render

# Create your views here.
def open(request):
	return render(request,'index1.html')

def show(request):
	return render(request,'index.html')
