from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True, label="Enter Password")
    
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True, label="Confirm password")

    class Meta:
        model = User
        fields = ['email', 'firstname', 'lastname', 'country', 'password', 'password2']
        extra_kwargs = {"password2": {"write_only": True}}

    def create(self, validated_data):
        email = validated_data["email"]
        fname = validated_data["firstname"]
        lname = validated_data["lastname"]
        password = validated_data["password"]
        password2 = validated_data["password2"]
        country_name = validated_data["country"]
        if (email and User.objects.filter(email=email).exists()):
            raise serializers.ValidationError(
                {"email": "Email addresses must be unique."})
        if password != password2:
            raise serializers.ValidationError(
                {"password": "The two passwords differ."})
        user = User(email=email, firstname=fname, lastname=lname, country=country_name)
        user.set_password(password)
        user.save()
        return user

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

