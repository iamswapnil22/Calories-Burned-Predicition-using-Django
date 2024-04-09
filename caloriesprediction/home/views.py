from django.shortcuts import render,HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse('This is the Home Page')
    return render(request,'base.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'base.html')
def prediction(request):
    # return render(request,'base.html')
    return HttpResponse('This is the Home Page')
