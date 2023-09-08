"""
URL configuration for quera_task_managements project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from qtask.views import Taskview ,ProjectView,OwnerView,Tagview

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
  
...
  
schema_view = get_schema_view(
   openapi.Info(
      title="Dummy API",
      default_version='v1',
      description="Dummy description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@dummy.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)




urlpatterns = [
    path('playground/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('tasks/<int:pk>/',Taskview.as_view()),
    path('tasks/',Taskview.as_view()),
    path('projects/',ProjectView.as_view()),
    path('projects/<int:pk>/',ProjectView.as_view()),
    path('owners',OwnerView.as_view()),
    path('owners/<int:pk>',OwnerView.as_view()),
    path('projects/<int:pk>/',OwnerView.as_view()),
    path('tags/<int:pk>/',Tagview.as_view()),
    path('tags/',Tagview.as_view()),


]
