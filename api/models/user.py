from mongoengine import Document,BooleanField, DateTimeField, StringField, EmailField, FloatField, DictField, EmbeddedDocument, ListField, EmbeddedDocumentField, ObjectIdField
# from background_task import background
# from .weekly_log import WeeklyLog
from datetime import datetime, timedelta
from .daily_log import DailyLog

class User(Document):
    # id = ObjectIdField(primary_key=True)
    name = StringField(required=True)
    phone_number = StringField()
    email = EmailField(required=True)
    address = StringField()
    password = StringField()
    profile_picture = StringField()
    gender = StringField()
    date_of_birth = StringField()
    image= StringField()

    daily_logs = ListField(EmbeddedDocumentField('DailyLog'), default=[])
    caloric_intake_goal = FloatField(default=0.0)
    daily_protein_goal = FloatField(default=0.0)
    daily_carb_goal = FloatField(default=0.0)
    daily_fat_goal = FloatField(default=0.0)
    goal = StringField(default="")
    tdee = FloatField(default=0.0)
    height = FloatField(default=0.0)
    current_weight = FloatField(default=0.0)
    
    first_login = BooleanField(default = True)
  
    meta = {
        'collection': 'users'  
    }

