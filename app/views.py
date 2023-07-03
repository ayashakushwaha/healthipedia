import os

from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from skimage import io
from keras.preprocessing import image
from keras import models
import numpy as np
import urllib
import pickle

def indexHandler(request):
    return render(request, "index.html")

def loginHandler(request):
    return render(request, "login.html")

def appointmentHandler(request):
    return render(request, "appointment.html")

def bmiHandler(request):
    return render(request, "bmi-calculator.html")

def malariaHandler(request):
    return render(request, "malaria.html")

def liverHandler(request):
    return render(request, "liver.html")

def liverResultHandler(request):
    liver_model = pickle.load(open("app/predictors/liver_model.pkl", 'rb'))
    liver_scaler = pickle.load(open("app/predictors/liver_scaler.pkl", 'rb'))

    data_param = urllib.parse.unquote(request.GET.get("data"))
    data = [ float(d) for d in data_param.split(",") ]
    data = liver_scaler.transform([data])
    prediction = liver_model.predict(data)[0]
    return render(request, "liver-result.html", {
        "prediction": prediction
    })

def diabetesHandler(request):
    return render(request, "diabetes.html")

def diabetesResultHandler(request):
    diabetes_model = pickle.load(open("app/predictors/diabetes_model.pkl", 'rb'))
    diabetes_scaler = pickle.load(open("app/predictors/diabetes_scaler.pkl", 'rb'))

    data_param = urllib.parse.unquote(request.GET.get("data"))
    data = [ float(d) for d in data_param.split(",") ]
    data = diabetes_scaler.transform([data])
    prediction = diabetes_model.predict(data)[0]
    return render(request, "diabetes-result.html", {
        "prediction": prediction
    })

def heartHandler(request):
    return render(request, "heart-disease.html")

def heartResultHandler(request):
    heart_disease_model = pickle.load(open("app/predictors/heart_disease_model.pkl", 'rb'))
    heart_disease_scaler = pickle.load(open("app/predictors/heart_disease_scaler.pkl", 'rb'))
    
    data_param = urllib.parse.unquote(request.GET.get("data"))
    data = [ float(d) for d in data_param.split(",") ]
    data = heart_disease_scaler.transform([data[:-1]])
    prediction = heart_disease_model.predict(data)[0]
    
    return render(request, "heart-result.html", {
        "prediction": prediction == "Presence"
    })

def breastCancerHandler(request):
    return render(request, "breast-cancer.html")

def breastCancerResultHandler(request):
    breast_cancer_model = pickle.load(open("app/predictors/breast_cancer_model.pkl", 'rb'))
    breast_cancer_scaler = pickle.load(open("app/predictors/breast_cancer_scaler.pkl", 'rb'))

    data_param = urllib.parse.unquote(request.GET.get("data"))
    data = [ float(d) for d in data_param.split(",") ]
    data = breast_cancer_scaler.transform([data])
    prediction = breast_cancer_model.predict(data)[0]
    return render(request, "breast-cancer-result.html", {
        "prediction": prediction
    })

def covidHandler(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(os.path.join("./app/templates/static/data", myfile.name), myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'covid.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'covid.html')

def covidResultHandler(request):
    data_param = urllib.parse.unquote(request.GET.get("data"))
    model = models.load_model("app/predictors/covid_19_model.h5")
    img = image.load_img(data_param[1:], grayscale=False, target_size=(64, 64))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis = 0)
    x /= 255

    custom = model.predict(x)
    prediction=np.argmax(custom[0])
    return render(request, "covid-result.html", {
        "img_url": data_param.split("/app/templates")[1],
        "prediction": prediction
    })