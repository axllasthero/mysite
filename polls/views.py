from django.shortcuts import render
from django.http import HttpResponse

from .models import Question, Choice
# Create your views here.
def index(request):
    q_all = Question.objects.all()
    res = "<ol>"
    for q in q_all:
        res += "<li>%s</li>" % q.text
    res += "</ol>"        
    return HttpResponse(res)


def detail(request, q_id):
    res = "Question number %s. " % q_id
    return HttpResponse(res)

def results(request, q_id):
    res = "Result for Question number %s. " % q_id
    return HttpResponse(res)

def vote(request, q_id):
    res = "Vote for Question number %s. " % q_id
    return HttpResponse(res)
    
    
    
    









def meme(request):
    return HttpResponse('<h1>why..... just why</h1><br><img src="https://img.ifunny.co/images/76b93d4f620e1db822719bbcf960103c8edbd136534e2de650c7bf281c4822a9_1.jpg">')
