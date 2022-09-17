from messReg.models import studentDetails
from rest_framework import serializers

class studentSerializer(serializers.Serializer):
    email = serializers.CharField()
    name = serializers.CharField()
    rollNo = serializers.CharField()
    gender = serializers.CharField()
    phoneNumber = serializers.IntegerField()
    
    def create(self, validated_data):
        return studentDetails.objects.create(**validated_data)
    
    
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.rollNo = validated_data.get('rollNo', instance.rollNo)
        instance.gender = validated_data.get('phoneNumber', instance.phoneNumber)
        instance.save()
        return instance
         
    
    
    
