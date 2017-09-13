# coding:utf-8
from rest_framework import serializers
from rest_framework.serializers import *
from .models import *

class userSerializer(serializers.ModelSerializer):
    #builds = serializers.PrimaryKeyRelatedField(many=True, queryset=user.objects.all())
    class Meta:
        model = user
        fields = ('user_id','user_pas','user_tel','user_account_id','user_designer_id','user_contractor_id')

class supplySerializer(serializers.ModelSerializer):     
    class Meta:
        model = supply
        fields = ('supply_id','supply_light','supply_tel','supply_wood','supply_floor','supply_name','supply_furniture','supply_delete')