from rest_framework import serializers
from .models import User, Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.username')
    recipient = serializers.ReadOnlyField(source='recipient.username')

    class Meta:
        model = Message
        fields = ['id', 'sender', 'recipient', 'content', 'timestamp']