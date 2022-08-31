from rest_framework_simplejwt.views import *
from django.urls import path
from .views import *
app_name = 'apis'

urlpatterns = [
    path('signup',SignupAPIView.as_view(), name='signup'),
    path('execute',EditorAPIView.as_view(), name='editor'),
    path('programs',MyProgramsAPIView.as_view(), name='programs'),
    
]