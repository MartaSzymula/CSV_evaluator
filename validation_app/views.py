from django.shortcuts import render, redirect
from django.views.generic import View
from .models import ValidationModel
from django.http import HttpResponse
import csv


class HomeView(View):
    def get(self, request):


        question = ValidationModel.objects.filter(answer=None).first()

        context = {
            'question' : question
        }


        return render(request, 'home.html', context)

class AnswerView(View):
    def post(self, request):

        id = request.POST.get('question_id')

        answer = request.POST.get('vote')
        comment = request.POST.get('comment')

        ValidationModel.objects.filter(id=id).update(answer=answer)
        ValidationModel.objects.filter(id=id).update(comment=comment)


        return redirect('/')

class UpdateView(View):

    def post(self, request):
        with open('validation_app\\static\\base_file.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                try:
                    ValidationModel.objects.get(synonym=row[0])
                except ValidationModel.DoesNotExist:
                    _, created = ValidationModel.objects.update_or_create(
                    synonym = row[0],
                    tag = row[1],
                    answer = None,
                    comment = row[3]
                    )

            return redirect('/')

class DownloadView(View):

    def post(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="output_file.csv"'

        writer = csv.writer(response)
        for i in ValidationModel.objects.all().values():
            writer.writerow([i['id'], i['synonym'], i['tag'], i['answer'], i['comment']])

        return response
