from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Dont type http://127.0.0.1:8000/polls/meme/</h1>")

def meme(request):
    return HttpResponse('<h1>Look Lois i am Django hosted site</h1><br><img src="https://upload.wikimedia.org/wikipedia/ru/5/5b/FamilyGuy_Peter_Griffin_72.jpg">')