from django.shortcuts import render
from rest_framework.decorators import api_view
from messReg.models import studentDetails
from rest_framework.response import Response
from messReg.serializers import studentSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def student_list(request):
    
    if request.method == 'GET':
        students = studentDetails.objects.all()
        serializer = studentSerializer(students, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = studentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    if request.method == 'GET':
        student =  studentDetails.objects.get(email=pk)
        serializer = studentSerializer(student)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        student =  studentDetails.objects.get(email=pk)
        serializer = studentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
            
        
    # if request.method =='PATCH':
        
    
    
