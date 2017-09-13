from rest_framework import status,generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from .models import *
from .serializer import *
# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = user.objects.all()
    serializer_class = userSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = user.objects.all()
    serializer_class = userSerializer

#提供url接口 ./supplyInfo
class get_all_supplyinfo(generics.ListCreateAPIView):
    queryset = supply.objects.all()
    serializer_class = supplySerializer

