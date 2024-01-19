from mongoengine import Document, DateTimeField, StringField, EmailField, DecimalField, DictField, EmbeddedDocument, ListField, EmbeddedDocumentField
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
    
    first_login = DateTimeField()
    @property
    def caloric_remain(self):
        today = datetime.now().date()
        today_logs = [log for log in self.daily_logs if log.date.date() == today]
        total_caloric_intake = sum(log.caloric_intake for log in today_logs)
        return max(0, self.caloric_intake_goal - total_caloric_intake)

    @property
    def protein_remain(self):
        today = datetime.now().date()
        today_logs = [log for log in self.daily_logs if log.date.date() == today]
        total_protein_intake = sum(log.protein_intake for log in today_logs)
        return max(0, self.daily_protein_goal - total_protein_intake)

    @property
    def carb_remain(self):
        today = datetime.now().date()
        today_logs = [log for log in self.daily_logs if log.date.date() == today]
        total_carb_intake = sum(log.carb_intake for log in today_logs)
        return max(0, self.daily_carb_goal - total_carb_intake)

    @property
    def fat_remain(self):
        today = datetime.now().date()
        today_logs = [log for log in self.daily_logs if log.date.date() == today]
        total_fat_intake = sum(log.fat_intake for log in today_logs)
        return max(0, self.daily_fat_goal - total_fat_intake)
    meta = {
        'collection': 'users'  
    }

