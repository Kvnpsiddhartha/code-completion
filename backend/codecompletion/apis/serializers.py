from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password','phone','photo']
class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['id', 'parent_folder','user', 'name','code','modified_time']

class FolderSerializer(serializers.ModelSerializer):
    programs=ProgramSerializer(many=True)
    class Meta:
        model = Folder
        fields = ['id', 'parent_folder','user', 'name','modified_time','programs']
    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['programs'] = [ProgramSerializer(instance.child).data for instance in response['programs']]
    #     return response
class EditorSerializer(serializers.Serializer):
    code=serializers.CharField(trim_whitespace=False)

class EditorOutputSerializer(serializers.Serializer):
    stdout=serializers.CharField(trim_whitespace=False)
    stderr=serializers.CharField(trim_whitespace=False)