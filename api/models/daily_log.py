from mongoengine import Document, DateTimeField, StringField, EmailField, FloatField, EmbeddedDocument, ListField, EmbeddedDocumentField
from .food import Food
from .exercise import Exercise
import datetime
class ExerciseSet(EmbeddedDocument):
    reps = FloatField(default=0)
    duration = FloatField(default=0)

class ExerciseData(EmbeddedDocument):
    sets = ListField(EmbeddedDocumentField('ExerciseSet'), default=[])
    exercise = EmbeddedDocumentField(Exercise)

class DailyLog(EmbeddedDocument):  
    date = DateTimeField(default=datetime.datetime.now().date().isoformat())

    caloric_intake = FloatField(default=0.0)
    protein_intake = FloatField(default=0.0)
    carb_intake = FloatField(default=0.0)
    fat_intake = FloatField(default=0.0)

    caloric_remain = FloatField(default=0.0)
    protein_remain = FloatField(default=0.0)
    carb_remain = FloatField(default=0.0)
    fat_remain = FloatField(default=0.0)

    caloric_intake_goal = FloatField(default=0.0)
    daily_protein_goal = FloatField(default=0.0)
    daily_carb_goal = FloatField(default=0.0)
    daily_fat_goal = FloatField(default=0.0)
    
    goal = StringField(default="")
    weight = FloatField(default=0.0)
    
    breakfast = ListField(EmbeddedDocumentField('Food'), default=[])
    lunch = ListField(EmbeddedDocumentField('Food'), default=[])
    dinner = ListField(EmbeddedDocumentField('Food'), default=[])

    exercise_data = ListField(EmbeddedDocumentField('ExerciseData'), default=[])
