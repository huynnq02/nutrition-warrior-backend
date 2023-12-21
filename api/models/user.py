from mongoengine import Document, StringField, EmailField, DecimalField, DictField, ReferenceField, ListField, LazyReferenceField, BooleanField

class User(Document):
    name = StringField(required=True)
    phone_number = StringField()
    email = EmailField(required=True)
    address = StringField()
    password = StringField(required=True)
    profile_picture = StringField()
    meta = {
        'collection': 'users'  # Specify the collection name as 'users'
    }