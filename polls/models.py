from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=512)
    pub_date = models.DateTimeField('date of publishion')

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    text = models.CharField(max_length=512)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.text
