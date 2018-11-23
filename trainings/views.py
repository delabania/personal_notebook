from django.shortcuts import render
from django.db.models import Max
from django.http import HttpResponse
from trainings.models import *
# Create your views here.

def exercise_personal_bests(request, exercise):
    personal_bests = Set.objects.filter(exercise__name=exercise).values(
        'additional_weight').annotate(Max('reps'))
    return HttpResponse(personal_bests)
