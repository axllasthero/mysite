from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name  = "questions"

    def get_queryset(self):
        return Question.objects.all()


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, q_id):
    choices = request.POST.getlist("choice")
    question = Question.objects.get(pk=q_id)
    for c_pk in choices:
        choice = question.choice_set.get(pk=c_pk)
        choice.votes += 1
        choice.save()
        
    return HttpResponseRedirect( reverse("polls:results", args=(q_id, )) )
    







def meme(request):
    return HttpResponse('<h1>why..... just why</h1><br><img src="https://img.ifunny.co/images/76b93d4f620e1db822719bbcf960103c8edbd136534e2de650c7bf281c4822a9_1.jpg">')
