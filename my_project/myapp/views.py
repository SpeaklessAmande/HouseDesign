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

class get_one_supplyinfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = supply.objects.all()
    serializer_class = supplySerializer

#查询用户所有的流水账单
@api_view(['GET','PUT','DELETE'])
def get_bill(request,pk,format=None):
    try:
        user_ = user.objects.get(pk=pk)
    except user.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        #获取用户表
        userrelated = userSerializer(user_).data
        #print(userrelated)
        try:
            user_money = account.objects.get(pk=userrelated['user_account_id'])
            user_money = accountSerializer(user_money).data
        except:
            try:
                user_money = designer.objects.get(pk=userrelated['user_designer_id'])
                user_money = designerSerializer(user_money).data
            #print(user_money)
            except:
                try:
                    user_money = contractor.objects.get(pk=userrelated['user_contractor_id'])
                    user_money = constractorSerializer(user_money).data
                except:
                    user_money = dict()
    return Response(user_money,status.HTTP_200_OK)

