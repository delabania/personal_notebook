from django.db import models

# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Training(models.Model):
    date = models.DateField()

    def __str__(self):
        return 'Training at {}'.format(self.date)

class Set(models.Model):
    training = models.ForeignKey(Training, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    additional_weight = models.IntegerField()
    reps = models.IntegerField()

    def __str__(self):
        return '{} - {} with +{}kg: {} reps'.format(
            self.training, self.exercise, self.additional_weight, self.reps)

class BodyWeight(models.Model):
    weight = models.FloatField()
    date = models.DateField()
