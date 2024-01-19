from mongoengine import Document,BooleanField, DateTimeField, StringField, EmailField, DecimalField, DictField, EmbeddedDocument, ListField, EmbeddedDocumentField
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

    daily_logs = ListField(EmbeddedDocumentField(DailyLog), default=[])
    caloric_intake_goal = DecimalField(default=0.0)
    daily_protein_goal = DecimalField(default=0.0)
    daily_carb_goal = DecimalField(default=0.0)
    daily_fat_goal = DecimalField(default=0.0)
    goal = StringField(default="")
    tdee = DecimalField(default=0.0)
    height = DecimalField(default=0.0)
    current_weight = DecimalField(default=0.0)
    
    first_login = BooleanField(default = True)
  
    meta = {
        'collection': 'users'  
    }

