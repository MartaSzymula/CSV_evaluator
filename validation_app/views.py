from django.shortcuts import render, redirect
from django.views.generic import View
# from django.db.models import Count

# from .models import Team, Player


class HomeView(View):
    def get(self, request):


        return render(request, 'home.html')
