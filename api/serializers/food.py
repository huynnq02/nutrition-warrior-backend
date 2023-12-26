from rest_framework_mongoengine.serializers import DocumentSerializer
from ..models.food import Food  

class FoodSerializer(DocumentSerializer):
    class Meta:
        model = Food
        fields = '__all__'  # Include all fields from the User model
