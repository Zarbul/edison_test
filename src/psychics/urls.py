from django.urls import path

from src.psychics import views

urlpatterns = [
    path('', views.index),
    path('input_number/', views.input_number, name='input_number'),
    path('predictions/', views.prediction),
    # path('results/', views.ResultView.as_view()),
]
