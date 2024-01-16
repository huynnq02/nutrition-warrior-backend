from mongoengine import Document, StringField, DateTimeField, EmailField
from datetime import datetime, timedelta

class OTP(Document):
    email = EmailField(required=True)
    otp_code = StringField(required=True)
    expiration_time = DateTimeField() 
    # unique_key = fields.StringField(required=True, unique=True)
    # Thêm các trường khác của bạn

    def save(self, *args, **kwargs):
        existing_document = OTP.objects(email=self.email).first()
        if existing_document:
            # Nếu document có cùng email tồn tại, cập nhật các trường khác
            existing_document.update(**self.to_mongo())
            return existing_document
        super().save(*args, **kwargs)
  
