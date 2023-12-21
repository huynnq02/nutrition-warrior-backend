from rest_framework_mongoengine.serializers import DocumentSerializer
from ..models.user import User  

class UserSerializer(DocumentSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Include all fields from the User model
