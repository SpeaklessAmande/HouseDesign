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

class AccountList(generics.ListCreateAPIView):
    queryset = account.objects.all()
    serializer_class = accountSerializer

class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = account.objects.all()
    serializer_class = accountSerializer


#*_set filter返回的queryset集合
#*_object get方法返回的对象


@api_view(['GET','POST'])
def login(request):
    if(request.method == 'POST'):
        user_set = user.objects.filter(user_tel__exact=request.data['user_tel'],user_pas__exact=request.data['user_pas'])
        if user_set:
            user_list = []
            for user_item in user_set:#filter返回queryset集合，需遍历
                if user_item.user_designer_id:#先判断是否设计师
                    user_type = 'designer'
                    designer_object = designer.objects.get(pk=user_item.user_designer_id.designer_id)
                    user_name = designer_object.designer_name
                elif user_item.user_account_id:#在判断是否普通用户
                    user_type = 'account'
                    account_object = account.objects.get(pk=user_item.user_account_id.account_id)
                    user_name = account_object.account_name
                elif user_item.user_constractor_id:#承包商
                    user_type = 'constractor'
                    constractor_object = constractor.objects.get(pk=user_item.user_constractor_id.constractor_id)
                    user_name = constractor_object.costractor_name
                #对返回数据的格式处理
                user_list.append({'user_id':user_item.user_id,'user_name':user_name,'user_type':user_type})

            return Response(user_list,status=status.HTTP_200_OK) 
    
    return  Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def blueprint_first(request):
    if (request.method == 'POST'):
        build_id = request.data['build_id']
        user_id = request.data['user_id']
        user_type = request.data['user_type']
        if (user_type == 'account'):
            #build_object = build.objects.get(pk=build_id)
            #log_object = 
            for log_item in log.objects.all():
                if(log_item.log_build_id.build_id == build_id):
                    log_object = log_item
                    break
            print(log_item.log_tender)
            log_result = logSerializer(log_item)
            result = []
            #先添加竞标节点信息
            result.append(log_result.data)
            comment_list = []
            i=1
            for comment_item in comment.objects.all():
                if(comment_item.comment_build_id.build_id == build_id and i<=6):
                    comment_list.append(comment_item)
                    i = i + 1 

            print(comment_list)
            comment_result = commentSerializer(comment_list,many=True)
            result.append(comment_result.data)
           
            #再添加评论信息
            build_object = build.objects.get(pk=build_id)
            build_item = buildSerializer(build_object)
            result.append(build_item.data)
            return Response(result,status=status.HTTP_200_OK)
        elif (user_type == 'designer'):
            result = []
            comment_list = []
            i=1
            for comment_item in comment.objects.all():
                if(comment_item.comment_build_id.build_id == build_id and i<=6):
                    comment_list.append(comment_item)
                    i = i + 1 

            print(comment_list)
            comment_result = commentSerializer(comment_list,many=True)
            result.append(comment_result.data)
           
            #再添加评论信息
            build_object = build.objects.get(pk=build_id)
            build_item = buildSerializer(build_object)
            result.append(build_item.data)
            return Response(result,status=status.HTTP_200_OK)
        elif (user_type == 'constractor'):
            result_constractor = []
            supply_list = supply.objects().all()
            supply_result = supplySerializer(supply_list,many=True)
            result_constractor.append(supply_result.data)
            build_object = build.objects.get(pk=build_id)
            build_item = buildSerializer(build_object)
            result_constractor.append(build_item.data)
            return Response(result_constractor,status=status.HTTP_200_OK)
            #   build = 
            #根据订单id查询所有供应商的所有信息
    return  Response(status=status.HTTP_204_NO_CONTENT)