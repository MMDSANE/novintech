from django.shortcuts import render
from question.models import Question

def competitions(request):
    questions = Question.objects.all()
    return render(request, "competitions.html", {"questions": questions})