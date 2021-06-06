from django.contrib.auth import get_user_model
from rest_framework import serializers
from datetime import datetime

User = get_user_model()

class UserFetchCovDataSerializer(serializers.ModelSerializer):
    timeline = serializers.DateTimeField(required=False, default=datetime.now())
    class Meta:
        model = User
        fields = ['country', 'timeline']