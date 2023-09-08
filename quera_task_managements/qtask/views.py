from django.shortcuts import render
from .models import Task,Project,Owner,Tags
from django.http import HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework import status
from . serializers import TaskSerializer,ProjectSerializer,OwnerSerializer,TagSerializer
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
class Taskview(generics.ListCreateAPIView):
    serializer_class=TaskSerializer

    def get_queryset(self):
        if self.request.method=="GET" and "pk" in self.kwargs:
            return Task.objects.filter(id=self.kwargs["pk"])
        else:
            return Task.objects.all()


        
    def perform_create(self,serializer):
        serializer.save()

class Tagview(generics.ListCreateAPIView):
    serializer_class=TagSerializer

    def get_queryset(self):
        if self.request.method=="GET" and "pk" in self.kwargs:
            return Tags.objects.filter(id=self.kwargs["pk"])
        else:
            return Tags.objects.all()


        
    def perform_create(self,serializer):
        serializer.save()

class ProjectView(generics.ListCreateAPIView):
    serializer_class=ProjectSerializer
    def get_queryset(self):
        if self.request.method=="GET" and "pk" in self.kwargs:
            return Project.objects.filter(id=self.kwargs["pk"])
        else:
            return Project.objects.all()


        
    def perform_create(self,serializer):
        serializer.save()

class OwnerView(generics.ListCreateAPIView,RetrieveModelMixin):

    serializer_class=OwnerSerializer


    def get_queryset(self):
        if self.request.method=="GET" and "pk" in self.kwargs:
            return Owner.objects.filter(id=self.kwargs["pk"])
        else:
            return Owner.objects.all()
        
    def perform_create(self,serializer):
        serializer.save()
