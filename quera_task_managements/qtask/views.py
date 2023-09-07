from django.shortcuts import render
from .models import Task,Project,Owner
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework import status
from . serializers import TaskSerializer,ProjectSerializer
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
  
  
class ContactForm(serializers.Serializer):
      # simple serializer for emails
    email = serializers.EmailField()
    message = serializers.CharField()
  
  
# simple endpoint to take the serializer data
class SendEmail(APIView):
      # permission class set to be unauthenticated
    permission_classes = (permissions.AllowAny,)
    # this is where the drf-yasg gets invoked
    @swagger_auto_schema(request_body=ContactForm)
    def post(self, request):
          # serializer object
        serializer = ContactForm(data=request.data)
        # checking for errors
        if serializer.is_valid():
            json = serializer.data
            return Response(
                data={"status": "OK", "message": json},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# Create your views here.
class Taskview(generics.ListCreateAPIView,RetrieveModelMixin,):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer

    def retrieve(self, request, *args, **kwargs):
        instance=self.get_object()
        serializer=self.get_serializer(instance)
        return serializer.data
    def perform_create(self,serializer):
        serializer.save()


class ProjectView(generics.ListCreateAPIView,RetrieveModelMixin):
    queryset=Project.objects.all()
    serializer_class=ProjectSerializer

    def retrieve(self, request, *args, **kwargs):
        instance=self.get_object()
        serializer=self.get_serializer(instance)
        return serializer.data
    def perform_create(self,serializer):
        serializer.save()
