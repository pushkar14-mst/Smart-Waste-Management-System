from django.shortcuts import render
import pyrebase
from matplotlib import pyplot as plt
from django.http import HttpResponse,JsonResponse

# Create your views here.
config={
    "apiKey": "AIzaSyDXsVZqLj_5HtfBCNtQ_zU1D6nKGSyZZ8Q",
    "authDomain": "esp01-test-1618c.firebaseapp.com",
    "databaseURL": "https://esp01-test-1618c-default-rtdb.firebaseio.com",
    "projectId": "esp01-test-1618c",
    "storageBucket": "esp01-test-1618c.appspot.com",
    "messagingSenderId": "803956331852",
    "appId": "1:803956331852:web:a6ba85b35b4c596fb22be9"
}
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

def home(request):
    warning_status=False
    gas=database.child('MiniProject').child('GasSensor').get().val()
    waste_level=database.child('MiniProject').child('UltrasonicSeonsor').get().val()
    if gas >900 or waste_level <5:
        warning_status=True
    context={
        "gas": gas, 
        "waste_level":waste_level,
        "warning_status":warning_status
    }
    return render(request,'waste_management/home.html',context)