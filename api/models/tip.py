from mongoengine import Document, StringField

class Tip(Document):
    title = StringField(max_length=255)
    explanation = StringField()

    meta = {
        'collection': 'tips'  
    }
