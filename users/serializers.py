from rest_framework import serializers
from .models import AppUser



class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AppUser
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'mobile', 'dob', 'gender', 'is_active', 'is_logged_in',] # 'latitude', 'longitude', 'location',
        read_only_fields = ('id', 'is_active', 'is_logged_in',)
        
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.dob = validated_data.get('dob', instance.dob)
        instance.save()
        return instance


class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ['id', 'first_name', 'last_name', 'email', 'mobile', 'dob', 'gender', 'username', 'is_active', 'is_logged_in',] # 'latitude', 'longitude', 'location',
        read_only_fields = ('id', 'mobile', 'email', 'is_active', 'is_logged_in',)


class UserLoginSerializer(serializers.Serializer):
    token = serializers.CharField()
    user = UserSerializer(read_only=True)


class UserRegisterSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=50)
    user = UserSerializer(read_only=True)
