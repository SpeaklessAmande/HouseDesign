from rest_framework import status,generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializer import *
import datetime
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

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
                user_money = build.objects.filter(build_designer=user_money['designer_id'])
            #print(user_money)
            except:
                try:
                    user_money = contractor.objects.get(pk=userrelated['user_contractor_id'])
                    user_money = contractorSerializer(user_money).data
                except:
                    user_money = dict()
    return Response(user_money,status.HTTP_200_OK)

@api_view(['GET','PUT','DELETE'])
def get_joinOrder(request,pk,format=None):
    try:
        build_ = build.objects.get(build_account_id=pk)
    except build.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    build_ = buildSerializer(build_)
    return Response(build_.data,status.HTTP_200_OK)


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
                elif user_item.user_contractor_id:#承包商
                    user_type = 'contractor'
                    contractor_object = contractor.objects.get(pk=user_item.user_contractor_id.contractor_id)
                    user_name = contractor_object.costractor_name
                #对返回数据的格式处理
                user_list.append({'user_id':user_item.user_id,'user_name':user_name,'user_type':user_type})

            return Response(user_list,status=status.HTTP_200_OK) 
    
    return  Response(status=status.HTTP_204_NO_CONTENT)
#{"build_id":1,"user_id":1,"user_type":"account"}
def getCommentList(build_id,user_id):
    #build_id = self.build_id
    #user_id = self.user_id
    comment_list = []
    i=1
    #print(comment.objects.all())
    for comment_item in comment.objects.all():
        if(comment_item.comment_build_id.build_id == build_id and i<=6):
            comment_end_item = {}
            if comment_item.comment_user_id.user_account_id.account_id:
               user_type = 'account'
               comment_name = account.objects.get(pk=comment_item.comment_user_id.user_account_id.account_id).account_name
            elif comment_item.comment_user_id.user_designer_id.designer_id:
                user_type = 'designer'
                comment_name = designer.objects.get(pk=comment_item.comment_build_id.user_designer_id.designer_id).designer_name
            
            comment_end_item['user_type'] = user_type
            comment_end_item['comment_name'] = comment_name
            comment_end_item['comment_content'] = comment_item.comment_content
            comment_list.append(comment_end_item)
            i = i + 1 

    print(comment_list)
    return comment_list

@api_view(['GET','POST'])
def blueprint_first(request):
    if (request.method == 'POST'):
        build_id = request.data['build_id']
        user_id = request.data['user_id']
        user_type = request.data['user_type']
        if (user_type == 'account'):
            #build_object = build.objects.get(pk=build_id)
            log_object = None
            for log_item in log.objects.all():
                if(log_item.log_build_id.build_id == build_id):
                    log_object = log_item
                    break
            node = 1
            if(log_object.log_accept != '1970-01-01'):
                node = 3
            elif(log_object.log_construction != '1970-01-01'):
                node = 2
            print(log_object.log_accept)
            print(node)
            #log_result = logSerializer(log_object)
            result = []
            #先添加竞标节点信息
            result.append(node)

            #comment_result = commentSerializer(comment_list,many=True)
            result.append(getCommentList(build_id,user_id))
            #result.append(comment_list)
            #再添加评论信息
            build_object = build.objects.get(pk=build_id)
            build_item = buildSerializer(build_object)
            result.append(build_item.data)
            return Response(result,status=status.HTTP_200_OK)
        elif (user_type == 'designer'):
            result = []
            #返回评论的信息：用户名、评论内容
            
            #comment_result = commentSerializer(getComm,many=True)
            result.append(getCommentList(build_id,user_id))
           
            #再添加评论信息
            build_object = build.objects.get(pk=build_id)
            build_item = buildSerializer(build_object)
            result.append(build_item.data)
            return Response(result,status=status.HTTP_200_OK)
        elif (user_type == 'contractor'):
            result_contractor = []
            supply_list = supply.objects.all()
            supply_result = supplySerializer(supply_list,many=True)
            result_contractor.append(supply_result.data)
            build_object = build.objects.get(pk=build_id)
            build_item = buildSerializer(build_object)
            result_contractor.append(build_item.data)
            return Response(result_contractor,status=status.HTTP_200_OK)
            #   build = 
            #根据订单id查询所有供应商的所有信息
    return  Response(status=status.HTTP_204_NO_CONTENT)
#{"comment_content":"contet","user_id":132,"build_id":1}
@api_view(['GET','POST'])
def addComment(request):
    if (request.method == 'POST'):
        #comment_content = request.data['comment_content']
        #build_id = request.data['build_id']
        #user_id = request.data['user_id']
        if(user.objects.filter(user_id=request.data["user_id"]).exists()==False):
            return Response("用户不存在",status=status.HTTP_400_BAD_REQUEST)
        comment_serializer = commentSerializer(data=request.data)
        if comment_serializer.is_valid():
            print(comment_serializer.data['comment_content'])
            comment_serializer.save()
        return Response(comment_serializer.data,status=status.HTTP_200_OK)
        
    return Response(status=status.HTTP_204_NO_CONTENT)        

@api_view(['GET','POST'])
def addBid(request):
    if(request.method == 'POST'):
        bid_serializer = bidSerializer(data=request.data)
        if bid_serializer.is_valid():
            bid_serializer.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def confirmNode(request):
    if(request.method == 'POST'):
        build_id = request.data['build_id']
        log_set = log.objects.filter(log_build_id_id__exact=build_id)
        for log_item in log_set:
            if(request.data['node_number']==3):
                log_item.log_accept = datetime.datetime.now().date()
            elif(request.data['node_number']==2):
                log_item.log_construction = datetime.datetime.now().date()
            else:
                log_item.log_tender = datetime.datetime.now().date()
            log_item.save()
            return Response(logSerializer(log_item).data,status=status.HTTP_200_OK)

    return Response(status=status.HTTP_204_NO_CONTENT)