from django.shortcuts import render
from rest_framework.decorators import api_view
from messReg.models import studentDetails
from rest_framework.response import Response
from messReg.serializers import studentSerializer 


# Create your views here.
@api_view()
def student_list(request):
    students = studentDetails.objects.all()
    serializer = studentSerializer(students, many=True)
    return Response(serializer.data)
    
@api_view()
def student_detail(request, pk):
    student =  studentDetails.objects.get(email=pk)
    serializer = studentSerializer(student)
    return Response(serializer.data)
    
    
