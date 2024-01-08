from mongoengine import Document, StringField, DateTimeField, EmailField
from datetime import datetime, timedelta

class OTP(Document):
    email = EmailField(unique=True)
    otp_code = StringField()
    expiration_time = DateTimeField()

  
