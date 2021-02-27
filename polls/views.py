from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Dont type http://127.0.0.1:8000/polls/meme/</h1>")

def meme(request):
    return HttpResponse('<h1>why..... just why</h1><br><img src="https://img.ifunny.co/images/76b93d4f620e1db822719bbcf960103c8edbd136534e2de650c7bf281c4822a9_1.jpg">')