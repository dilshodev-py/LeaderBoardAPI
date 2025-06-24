from django.urls import path
from .views import AddCoinsToStudentAPIView, StudentCreateAPIView, StudentListAPIView

urlpatterns = [
    path("student/add-coin/<int:student_id>", AddCoinsToStudentAPIView.as_view(), name="add-coin"),
    path("student/create", StudentCreateAPIView.as_view()),
    path("student/list", StudentListAPIView.as_view()),

]