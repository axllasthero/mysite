from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {
        "questions" : questions
    }
    return render(request, "index.html", context)


def detail(request, q_id):
    question = Question.objects.get(pk=q_id)
    context = {
        "question" : question,
    }
    return render(request, "detail.html", context)



def vote(request, q_id):
    choices = request.POST.getlist("choice")
    question = Question.objects.get(pk=q_id)
    for c_pk in choices:
        choice = question.choice_set.get(pk=c_pk)
        choice.votes += 1
        choice.save()
        


    return HttpResponseRedirect( reverse("polls:results", args=(q_id, )) )
    
    
def results(request, q_id):
    question = Question.objects.get(pk=q_id)
    context = {
        "question" : question,
    }
    return render(request, "results.html", context)
    









def meme(request):
    return HttpResponse('<h1>why..... just why</h1><br><img src="https://img.ifunny.co/images/76b93d4f620e1db822719bbcf960103c8edbd136534e2de650c7bf281c4822a9_1.jpg">')
