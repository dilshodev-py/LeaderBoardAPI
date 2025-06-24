from rest_framework import serializers

from apps.models import Student


class AddCoinsToStudentSerializer(serializers.Serializer):
    coin = serializers.IntegerField(min_value=1)


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"