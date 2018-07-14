from django.db import models

# Create your models here.

class Performance(models.Model):
    key = models.CharField(max_length=100)
    smile = models.IntegerField(default=-1)
    speech_rate = models.IntegerField(default=-1)
    emotion = models.IntegerField(default=-1)
    filler_words = models.IntegerField(default=-1)
    eye_contact = models.IntegerField(default=-1)
    nervousness = models.IntegerField(default=-1)
    pause = models.IntegerField(default=-1)
    clearness = models.IntegerField(default=-1)
    createdOn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key

    class Meta:
        ordering = ('-createdOn',)