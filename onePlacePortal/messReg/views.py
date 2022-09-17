from django.shortcuts import render
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from messReg.models import studentDetails
from rest_framework.response import Response
from rest_framework import status
from messReg.serializers import studentSerializer


# Create your views here.
class StudentListAV(APIView):
    def get(self, request):
        students = studentDetails.objects.all()
        serializer = studentSerializer(students, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = studentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class StudentDetailAV(APIView):
    def get(self, request, pk):
        try:
            student =  studentDetails.objects.get(email=pk)
        except studentDetails.DoesNotExist:
            return Response({"Error": "Student Details Not Found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = studentSerializer(student)
        return Response(serializer.data)
    
    def put(self, request, pk):
        student =  studentDetails.objects.get(email=pk)
        serializer = studentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        try:
            student = studentDetails.objects.get(email=pk)
        except studentDetails.DoesNotExist:
            return Response({'error': 'The student is not in the list'})
        student.delete()
        return Response({'success': 'The data is deleted'})
        
        
        
        
        
        


# @api_view(['GET', 'POST'])
# def student_list(request):
    
#     if request.method == 'GET':
        # students = studentDetails.objects.all()
        # serializer = studentSerializer(students, many=True)
        # return Response(serializer.data)
    
#     if request.method == 'POST':
        # serializer = studentSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors)
        

# @api_view(['GET', 'PUT', 'DELETE'])
# def student_detail(request, pk):
#     if request.method == 'GET':
        
        # try:
        #     student =  studentDetails.objects.get(email=pk)
        # except studentDetails.DoesNotExist:
        #     return Response({"Error": "Student Details Not Found"}, status=status.HTTP_404_NOT_FOUND)
        # serializer = studentSerializer(student)
        # return Response(serializer.data)
    
#     if request.method == 'PUT':
        # student =  studentDetails.objects.get(email=pk)
        # serializer = studentSerializer(student, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors)
    
    
            
#     if request.method =='DELETE':
        # student = studentDetails.objects.get(email=pk)
        # student.delete()
        # return Response({'success': 'The data is deleted'})
        
    
    
