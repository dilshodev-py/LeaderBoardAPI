from rest_framework import views, generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializers import AddCoinsToStudentSerializer

from rest_framework.generics import CreateAPIView

class AddCoinsToStudentAPIView(views.APIView):
    permission_classes = [IsAuthenticated]
from apps.models import Student
from apps.serializers import StudentModelSerializer

    def post(self, request, student_id):
        serializer = AddCoinsToStudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        coin_amount = serializer.validated_data.get("coin")

        student = get_object_or_404(Student, id=student_id)
        student.coin += coin_amount
        student.save()

        return Response({"message": f"{coin_amount} coins added successfully."}, status=status.HTTP_200_OK)

class StudentCreateAPIView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer