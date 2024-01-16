from rest_framework_mongoengine.serializers import DocumentSerializer
from ..models.otp import OTP

class OTPSerializer(DocumentSerializer):
    class Meta:
        model = OTP
        fields = '__all__'

