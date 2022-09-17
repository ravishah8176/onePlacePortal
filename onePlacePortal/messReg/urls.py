from django.urls import path, include
from messReg.views import student_list, student_detail


urlpatterns = [
    path('list/', student_list, name='student-list'),
    path('<str:pk>/', student_detail, name='student-detail')
]