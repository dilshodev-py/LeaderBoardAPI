from rest_framework.generics import CreateAPIView

from apps.models import Student
from apps.serializers import StudentModelSerializer


class StudentCreateAPIView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer