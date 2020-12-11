from django.shortcuts import render, redirect
from django.views.generic import View
from .models import ValidationDB
# from django.contrib import messages

import csv, random


class HomeView(View):
    def get(self, request):
        question = ValidationDB.objects.filter(answer="").first()

        # for question in questions:


        context = {
            'question' : question
        }


        return render(request, 'home.html', context)

    def post(self, request):
        # question = ValidationDB.objects.get(id=id)

        id = request.POST.get('question_id')

        answer = request.POST.get('vote')
        #
        # question.update(answer=answer)
        print(id)
        print(answer)
        ValidationDB.objects.filter(id=id).update(answer=answer)


        return redirect('/')

    def CSVimport(request):
        with open('/fixtures/base_file.csv') as f:
            reader = csv.reader(f)
        for column in reader:
            _, created = ValidationDB.objects.get_or_create(
            synonym = column[0],
            tag = column[1],
            )


            return render(request)
