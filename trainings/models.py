from django.db import models

# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=50)

class Training(models.Model):
    date = models.DateField()

class Set(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    additional_weight = models.IntegerField()
    reps = models.IntegerField()

class BodyWeight(models.Model):
    weight = models.FloatField()
    date = models.DateField()
