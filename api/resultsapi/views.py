from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import generics,permissions
from .serializers import StudentSerializer,ResultsSerializer,EmailSerializer
from resultsapi.models import Student
from django.db import transaction

class StudentRegisterView(generics.CreateAPIView):
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]

    @transaction.atomic
    def create(self, request: Request) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class CheckResultsView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self,request,*args, **kwargs):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            try:
                student = Student.objects.get(email=email)
                if student is not None:
                    returned_data = {
                        "student": {
                            "email": student.email,
                            "first_name": student.first_name,
                            "subject_1": student.subject_1,
                            "subject_2": student.subject_2,
                            "subject_3": student.subject_3,
                            "subject_4": student.subject_4,
                            "subject_5": student.subject_5,
                            "subject_1_score": student.subject_1_score,
                            "subject_2_score": student.subject_2_score,
                            "subject_3_score": student.subject_3_score,
                            "subject_4_score": student.subject_4_score,
                            "subject_5_score": student.subject_5_score,
                        }
                    }
                    return Response(
                        {
                            "data": returned_data,
                            "message": "student fetched successfully",
                            "status": True,
                            "status_code": 0,
                        },status=status.HTTP_200_OK,
                    )
                else:
                    return Response(
                        {
                            "message": "You did not register for this exam",
                            "data": {},
                            "status": False,
                            "status_code": 1,
                        },status=status.HTTP_400_BAD_REQUEST,
                    )

            except Student.DoesNotExist:
                        return Response(
                            {
                                "message": "Invalid email address",
                                "data": {},
                                "status": False,
                                "status_code": 1,
                            },
                            status=status.HTTP_400_BAD_REQUEST,
                        )
        else:
            return Response(
                {
                    "message": serializer.errors,
                    "data": {},
                    "status": False,
                    "status_code": 1,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
