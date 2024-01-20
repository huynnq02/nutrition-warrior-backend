from mongoengine import Document, StringField, FloatField, DictField, ListField, EmbeddedDocument, EmbeddedDocumentField

class Exercise(EmbeddedDocument):
    bodyPart = StringField(required=True)
    equipment = StringField(required=True)
    gifUrl = StringField(required=True)
    name = StringField(required=True)
    target = StringField(required=True)
    secondaryMuscles = ListField(StringField())
    instructions = ListField(StringField())

    meta = {
        'collection': 'exercises'
    }
