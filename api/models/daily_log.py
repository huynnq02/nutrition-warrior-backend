from mongoengine import Document, DateTimeField, StringField, EmailField, DecimalField, EmbeddedDocument, ListField, EmbeddedDocumentField
from .food import Food
from .exercise import Exercise
import datetime
class ExerciseSet(EmbeddedDocument):
    reps = DecimalField(default=0)
    duration = DecimalField(default=0)

class ExerciseData(EmbeddedDocument):
    sets = ListField(EmbeddedDocumentField(ExerciseSet), default=[])
    exercise = EmbeddedDocumentField(Exercise)

class DailyLog(EmbeddedDocument):  
    date = DateTimeField(default=datetime.datetime.now().date())

    caloric_intake = DecimalField(default=0.0)
    protein_intake = DecimalField(default=0.0)
    carb_intake = DecimalField(default=0.0)
    fat_intake = DecimalField(default=0.0)

    weight = DecimalField(default=0.0)
    
    breakfast = ListField(EmbeddedDocumentField(Food), default=[])
    lunch = ListField(EmbeddedDocumentField(Food), default=[])
    dinner = ListField(EmbeddedDocumentField(Food), default=[])

    exercise_data = ListField(EmbeddedDocumentField(ExerciseData), default=[])
