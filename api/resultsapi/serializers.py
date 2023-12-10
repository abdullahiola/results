from rest_framework import serializers
from typing import Any
import random
from resultsapi.models import Student

def generate_random_score():
    return random.randint(0, 99)

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = [
            "email", "first_name", "last_name",'state','subject_1',
            'subject_2', 'subject_3', 'subject_4','subject_5'
        ]

    def create(self, validated_data: dict[str, Any]) -> Student:
        """Create a new student."""

        student = Student.objects.create(**validated_data)
    
        student.subject_1_score = generate_random_score()
        student.subject_2_score = generate_random_score()
        student.subject_3_score = generate_random_score()
        student.subject_4_score = generate_random_score()
        student.subject_5_score = generate_random_score()
        
        student.save()
        
        return student


class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "email", "first_name", "last_name",'state','subject_1',
            'subject_2', 'subject_3', 'subject_4','subject_5','subject_1_score','subject_2_score',
            'subject_3_score','subject_4_score','subject_5_score'
        ]


class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        """Validate that user with email exists."""
        user = Student.objects.filter(email=value)

        if not user:
            raise serializers.ValidationError(
                "Invalid email address. No student with this credentials was found."
            )

        return value