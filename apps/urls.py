from django.urls import path
from .views import AddCoinsToStudentAPIView


urlpatterns = [
    path("student/add-coin/<int:student_id>", AddCoinsToStudentAPIView.as_view(), name="add-coin")
]