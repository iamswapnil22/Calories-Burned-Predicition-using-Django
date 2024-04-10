from django.shortcuts import render,HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse('This is the Home Page')
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def prediction(request):
    return render(request,'prediction.html')
