from mongoengine import Document, DateTimeField, StringField, EmailField, DecimalField, EmbeddedDocument, ListField, EmbeddedDocumentField
from .food import Food

class DailyLog(EmbeddedDocument):  
    date = DateTimeField(required=True) # DD/MM/YYYY 

    caloric_intake = DecimalField()
    protein_intake = DecimalField()
    carb_intake = DecimalField()
    weight = DecimalField()
    
    breakfast = ListField(EmbeddedDocumentField(Food))
    lunch = ListField(EmbeddedDocumentField(Food))
    dinner = ListField(EmbeddedDocumentField(Food))