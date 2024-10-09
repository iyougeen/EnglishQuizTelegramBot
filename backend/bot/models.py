from django.db import models


# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=200, blank=True)
    translate = models.CharField(max_length=200, blank=True)
    last_picked = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.word


class Player(models.Model):
    first_name = models.CharField(max_length=200, blank=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    user_id = models.IntegerField()
    num_right_answers = models.IntegerField()
    num_wrong_answers = models.IntegerField()

    def __str__(self):
        return self.first_name


class Poll(models.Model):
    poll_id = models.CharField(max_length=200, blank=True)
    poll_question = models.CharField(max_length=200, blank=True)
    poll_right_asnwer = models.CharField(max_length=200, blank=True)
    poll_right_asnwer_id = models.IntegerField()
    date_create = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.poll_question
