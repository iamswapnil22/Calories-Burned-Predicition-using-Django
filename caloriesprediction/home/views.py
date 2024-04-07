from django.shortcuts import render,HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse('This is the Home Page')
    return render(request,'base.html')

def about(request):
    return HttpResponse('This is about Page')