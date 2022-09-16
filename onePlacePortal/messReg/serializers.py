from rest_framework import serializers

class studentSerializer(serializers.Serializer):
    email = serializers.EmailField(read_only=True)
    name = serializers.CharField()
    rollNo = serializers.CharField()
    gender = serializers.CharField()
    phoneNumber = serializers.IntegerField()
    
    
    
    
