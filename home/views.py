from django.shortcuts import render,HttpResponse
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle
from sklearn.ensemble import RandomForestRegressor
from django.core.exceptions import ValidationError
import os

# Create your views here.

def index(request):
    # return HttpResponse('This is the Home Page')
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
# def prediction(request):
#     if request.method == "POST":
#         height = float(request.POST.get('height'))
#         age = float(request.POST.get('age'))
#         weight= float(request.POST.get('weight'))
#         duration= float(request.POST.get('duration'))
#         heart_Rate = float(request.POST.get('heart_Rate'))
#         temprature = int(request.POST.get('temprature'))
#         gender = int(request.POST.get('gender'))

#         print(request.POST)
#         print(age,height)
#     else:
#         return render(request,'prediction.html')
def abc(request):
    return render(request,'abc.html')

def prediction(request):
    if request.method == 'POST':
        # Get form data and convert to desired data types
            BMI = float(request.POST.get('BMI'))
            age = int(request.POST.get('Age'))
            # weight = float(request.POST.get('Weight'))
            duration = float(request.POST.get('Duration'))
            heart_rate = float(request.POST.get('Heart_Rate'))
            temperature = float(request.POST.get('Temperature'))
            gender = int(request.POST.get('Gender'))

            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

            model_path = os.path.join(BASE_DIR, 'static', 'calories_burned_model.pkl')
            print(model_path)

            with open(model_path, 'rb') as file:
                model = pickle.load(file)
                print(model)
            
            
            input_array = np.asarray([age,BMI,duration,heart_rate,temperature,gender]).reshape(1,-1)
            prediction = model.predict(input_array)
            prediction = round(prediction[0] , 2)
            print("prediction",prediction)

            context = {'output': prediction}  # Set initial output as empty
            return render(request, 'prediction.html', context)
    else:
    # Handle non-GET requests (optional)
        return render(request, 'prediction.html')
