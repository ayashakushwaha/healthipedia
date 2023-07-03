from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexHandler),
    path("login/", views.loginHandler),
    path("appointment/", views.appointmentHandler),
    path("bmi-calculator/", views.bmiHandler),
    path("liver-disease/", views.liverHandler),
    path("liver-disease/result/", views.liverResultHandler),
    path("diabetes/", views.diabetesHandler),
    path("diabetes/result/", views.diabetesResultHandler),
    path("heart-disease/", views.heartHandler),
    path("heart-disease/result/", views.heartResultHandler),
    path("breast-cancer/", views.breastCancerHandler),
    path("breast-cancer/result/", views.breastCancerResultHandler),
    path("covid/", views.covidHandler),
    path("covid/result", views.covidResultHandler),
]