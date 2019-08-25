from .models import Student,Student2
from rest_framework.serializers import ModelSerializer



class StudentSerializer(ModelSerializer):
    print('inside StudentSerializer')
    class Meta:
        model = Student
        fields = '__all__'


class Student2Serializer(ModelSerializer):
    print('inside Student2Serializer')
    class Meta:
        model = Student2
        fields = '__all__'