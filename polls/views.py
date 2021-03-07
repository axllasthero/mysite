from django.shortcuts import render
from django.http import HttpResponse

from .models import Question, Choice
# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {
        "questions" : questions
    }
    return render(request, "index.html", context)


def detail(request, q_id):
    questions = Question.objects.get(pk=q_id)
    context = {
        "questions" : questions
    }
    return HttpResponse(request, "polls/index.html", context)

def results(request, q_id):
    res = "Result for Question number %s. " % q_id
    return HttpResponse(res)

def vote(request, q_id):
    res = "Vote for Question number %s. " % q_id
    return HttpResponse(res)
    
    
    
    









def meme(request):
    return HttpResponse('<h1>why..... just why</h1><br><img src="https://img.ifunny.co/images/76b93d4f620e1db822719bbcf960103c8edbd136534e2de650c7bf281c4822a9_1.jpg">')
