from django.shortcuts import render, redirect
from django.views.generic import View
from .models import ValidationDB
from django.http import HttpResponse
import csv


class HomeView(View):
    def get(self, request):


        question = ValidationDB.objects.filter(answer="").first()

        context = {
            'question' : question
        }


        return render(request, 'home.html', context)

class AnswerView(View):
    def post(self, request):
        # question = ValidationDB.objects.get(id=id)

        id = request.POST.get('question_id')

        answer = request.POST.get('vote')

        ValidationDB.objects.filter(id=id).update(answer=answer)


        return redirect('/')

class UpdateView(View):

    def post(self, request):
        with open('validation_app\\static\\base_file.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                try:
                    ValidationDB.objects.get(synonym=row[0])
                except ValidationDB.DoesNotExist:
                    _, created = ValidationDB.objects.update_or_create(
                    synonym = row[0],
                    tag = row[1],
                    answer = row[2]
                    )

            return redirect('/')

class DownloadView(View):

    def post(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="output_file.csv"'

        writer = csv.writer(response)
        for i in ValidationDB.objects.all().values():
            writer.writerow([i['id'], i['synonym'], i['tag'], i['answer']])

        return response
