from mongoengine import Document, StringField, EmailField, DecimalField, DictField, EmbeddedDocument, ListField, EmbeddedDocumentField
# from background_task import background
# from .weekly_log import WeeklyLog
from datetime import datetime, timedelta
from .daily_log import DailyLog

class User(Document):
    name = StringField(required=True)
    phone_number = StringField()
    email = EmailField(required=True)
    address = StringField()
    password = StringField(required=True)
    profile_picture = StringField()
    gender = StringField()
    date_of_birth = StringField()

    daily_logs = ListField(EmbeddedDocumentField(DailyLog))
    caloric_intake_goal = DecimalField()
    daily_protein_goal = DecimalField()
    daily_carb_goal = DecimalField()
    daily_fat_goal = DecimalField()
    goal = StringField()
    tdee = DecimalField()
    height = DecimalField()
    current_weight = DecimalField()

    meta = {
        'collection': 'users'  
    }

