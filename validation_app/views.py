from django.shortcuts import render, redirect
from django.views.generic import View
from .models import ValidationDB
from django.http import HttpResponse
import csv


class HomeView(View):
    def get(self, request):

        with open('validation_app\\static\\base_file.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                _, created = ValidationDB.objects.update_or_create(
                synonym = row[0],
                tag = row[1],
                answer = row[2]
                )
                print(row)

        question = ValidationDB.objects.filter(answer="").first()

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
    #

    def CSVExport(request):

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="output_file.csv"'

        writer = csv.writer(response)

        writer.writerow(['First row', ValidationDB.objects.all()])
        writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

        return response
