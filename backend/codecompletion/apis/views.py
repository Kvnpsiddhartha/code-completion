from sys import stdout
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import *
from .models import *
import subprocess
import os
from codecompletion.settings import BASE_DIR
# Create your views here.
class SignupAPIView(generics.CreateAPIView):
    serializer_class=UserSerializer
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='username'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='password'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='email'),
                'phone': openapi.Schema(type=openapi.TYPE_STRING, description='phone'),
                'photo': openapi.Schema(type=openapi.TYPE_FILE, description='phone'),
            }
        ),
        required=['username','password','email','phone','photo'],
        responses={
            201: "created",
            400: "not valid",
        }
    )
    def post(self, request):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class EditorAPIView(generics.GenericAPIView):
    serializer_class=EditorSerializer
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'code': openapi.Schema(type=openapi.TYPE_STRING, description='code'),
            }
        ),
        required=['code'],
        # responses={
        #     201: "created",
        #     400: "not valid",
        # }
    )
    def post(self, request):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code=serializer.data.get("code")
        f = open(os.path.join(BASE_DIR, "media/temp.c"), 'w') 
        f.write(code) 
        f.close()
        out1=[b"",b""]
        out2=[b"",b""]
        p1 = subprocess.Popen(["gcc","-o",os.path.join(BASE_DIR, "media/a.exe"),os.path.join(BASE_DIR, "media/temp.c")],  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out1=p1.communicate()
        if not out1[1]:
            p2 = subprocess.Popen([os.path.join(BASE_DIR, "media","a.exe")],  stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out2=p2.communicate()
        
        
        # p1.stdout.flush()
        # p1.stderr.flush()
        # p2.stdout.flush()
        # p2.stderr.flush()
        out=[(out1[0]+out2[0]).decode('utf-8'),(out1[1]+out2[1]).decode('utf-8')]
        out=[out[0].replace('\r\n',"<br/>").strip(),out[1].replace('\r\n',"<br/>").strip()]
        # out=p.stdout.read()
        # test=subprocess.run(["gcc","-o",os.path.join(BASE_DIR, "media/a.exe"),os.path.join(BASE_DIR, "media/temp.c")], capture_output=True)

        # subprocess.call(["gcc","-o",os.path.join(BASE_DIR, "media/a.exe"),os.path.join(BASE_DIR, "media/temp.c")])
        
        # out=subprocess.check_output(["gcc","-o",os.path.join(BASE_DIR, "media/a.exe"),os.path.join(BASE_DIR, "media/temp.c")])
        # out+=subprocess.check_output(os.path.join(BASE_DIR, "media","a.exe"))

        # p=subprocess.Popen([os.path.join(BASE_DIR, "media","a.exe")], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # stdout_data,stderr_data=p.communicate()
        # output=stdout_data+stderr_data

        # with open(os.path.join(BASE_DIR,"media/out.txt"),"wb") as out, open(os.path.join(BASE_DIR,"media/err.txt"),"wb") as err:
        # subprocess.call(os.path.join(BASE_DIR, "media/a.exe"),stdout=buffer.fileno(),stderr=buffer.fileno())
        # f=open(os.path.join(BASE_DIR,"media/out.txt"))
        # output=f.read()
        # f.close()
        # f=open(os.path.join(BASE_DIR,"media/err.txt"))
        # output+=f.read()
        # f.close()
        # serializer=EditorOutputSerializer({"stdout":test.stdout,"stderr":test.stderr})
        return Response(out, status=status.HTTP_202_ACCEPTED)


class MyProgramsAPIView(generics.ListCreateAPIView):
    serializer_class=FolderSerializer
    queryset=Folder.objects.all()
