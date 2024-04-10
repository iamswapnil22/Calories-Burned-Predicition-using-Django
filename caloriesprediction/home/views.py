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
    if request.method == "POST":
        height = float(request.POST.get('height'))
        age = float(request.POST.get('age'))
        weight= float(request.POST.get('weight'))
        duration= float(request.POST.get('duration'))
        heart_Rate = float(request.POST.get('heart_Rate'))
        temprature = int(request.POST.get('temprature'))
        gender = int(request.POST.get('gender'))

        print(request.POST)
        print(age,height)
    else:
        return render(request,'prediction.html')
