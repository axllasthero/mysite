from django.urls import path

from . import views

urlpatterns = [
    path('polls/', views.index, name="index"),
    path('meme/', views.meme, name="meme"),
    path('<int:q_id>/', views.detail, name="detali"),
    path('<int:q_id>/results/', views.results, name="result"),
    path('<int:q_id>/vote/', views.vote, name="vote"),

]