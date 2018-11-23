
from django.urls import path
from trainings.views import exercise_personal_bests

urlpatterns = [
    path(r'personal_bests/<str:exercise>/', exercise_personal_bests)
]