from django.urls import path

from apps.views import StudentCreateAPIView

urlpatterns = [
    path('students/create', StudentCreateAPIView.as_view())
]
