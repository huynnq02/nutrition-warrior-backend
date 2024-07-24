from mongoengine import Document, StringField

class Key(Document):
    key = StringField(required=True)

    meta = {
        'collection': 'keys',
        'strict': False  
    }
