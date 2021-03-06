from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('submitanswer/', views.AnswerView.as_view()),
    path('csvdownload/', views.DownloadView.as_view()),
    path('csvupdate/', views.UpdateView.as_view()),

]
