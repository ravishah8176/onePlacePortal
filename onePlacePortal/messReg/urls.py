from django.urls import path, include
from messReg.views import StudentDetailAV, StudentListAV


urlpatterns = [
    path('list/', StudentListAV.as_view(), name='student-list'),
    path('<str:pk>/', StudentDetailAV.as_view(), name='student-detail')
]