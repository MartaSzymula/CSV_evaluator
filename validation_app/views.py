from django.shortcuts import render, redirect
from django.views.generic import View
from .models import ValidationDB


class HomeView(View):
    def get(self, request):
        questions = ValidationDB.objects.all()

        context = {
            'questions' : questions
        }


        return render(request, 'home.html', context)
