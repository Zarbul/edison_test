from django.urls import path

from src.psychics import views

urlpatterns = [
    path('', views.InputNumberView.as_view()),
    path('predictions/', views.prediction),
    path('results/', views.ResultView.as_view()),
]
