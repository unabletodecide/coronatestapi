from rest_framework import serializers
from datetime import datetime

class UserFetchCovDataSerializer(serializers.Serializer):
    timeline = serializers.DateTimeField(required=False, allow_null=True, default=datetime.now())
    country = serializers.CharField(required=False)