from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Notes


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}
    """
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data.get('email', '')
        )
        user.set_password(validated_data['password'])  # ✅ Hash the password
        
        # Assign role based on email structure
        email = user.email.lower()
        if email.endswith("@student.edu"):
            group_name = "Student"
        elif email.endswith("@lecturer.edu"):
            group_name = "Lecturer"
        elif email.endswith("@admin.edu"):
            group_name = "Admin"
        else:
            group_name = "Default"  # Assign a default group if no match

        user.save()

        # Add user to the correct group
        group, _ = Group.objects.get_or_create(name=group_name)  # Create group if it doesn't exist
        user.groups.add(group)

        return user
    """

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}