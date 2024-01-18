from mongoengine import Document, DateTimeField, StringField, EmailField, DecimalField, EmbeddedDocument, ListField, EmbeddedDocumentField
from .food import Food
from .exercise import Exercise

class ExerciseSet(EmbeddedDocument):
    reps = DecimalField()
    duration = DecimalField()

class ExerciseData(EmbeddedDocument):
    sets = ListField(EmbeddedDocumentField(ExerciseSet))
    exercise = EmbeddedDocumentField(Exercise)

class DailyLog(EmbeddedDocument):  
    date = DateTimeField(required=True)

    caloric_intake = DecimalField()
    protein_intake = DecimalField()
    carb_intake = DecimalField()
    weight = DecimalField()
    
    breakfast = ListField(EmbeddedDocumentField(Food))
    lunch = ListField(EmbeddedDocumentField(Food))
    dinner = ListField(EmbeddedDocumentField(Food))

    exercise_data = ListField(EmbeddedDocumentField(ExerciseData))
