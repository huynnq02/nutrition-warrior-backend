from mongoengine import Document, StringField, DecimalField, DictField, ListField, EmbeddedDocument, EmbeddedDocumentField

class Exercise(EmbeddedDocument):
    body_part = StringField(required=True)
    equipment = StringField(required=True)
    gif_url = StringField(required=True)
    name = StringField(required=True)
    target = StringField(required=True)
    secondary_muscles = ListField(StringField())
    instructions = ListField(StringField())

    meta = {
        'collection': 'exercises'
    }
