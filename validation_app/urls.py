from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    # path('validation/', views.ValidationView.as_view()),

]
