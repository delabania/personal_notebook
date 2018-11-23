from django.contrib import admin

from trainings.models import Exercise, Set, Training, BodyWeight
# Register your models here.

@admin.register(Exercise)
class Exercise(admin.ModelAdmin):
    pass

@admin.register(Set)
class Set(admin.ModelAdmin):
    pass

@admin.register(Training)
class Training(admin.ModelAdmin):
    pass

@admin.register(BodyWeight)
class BodyWeight(admin.ModelAdmin):
    pass
