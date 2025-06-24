from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class AddCoinsToStudentSerializer(serializers.Serializer):
    coin = serializers.IntegerField(min_value=1)