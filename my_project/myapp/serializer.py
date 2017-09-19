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

class buildSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=build
        fields=('build_id','build_name','build_account_id','build_designer','build_blueprint','build_blueprint_price','build_date','build_wood','build_wood_price','build_light','build_light_price','build_floor','build_floor_price','build_furniture','build_furniture_price','build_supply','build_contractor','build_delete_status')

class logSerializer(serializers.ModelSerializer):

    class Meta:
        model=log
        fields=('log_id','log_build_id','log_tender','log_construction','log_accept')

class commentSerializer(serializers.ModelSerializer):

    class Meta:
        model=comment 
        fields=('comment_id','comment_content','comment_time','comment_build_id','comment_user_id')

class contractorSerializer(serializers.ModelSerializer):

    class Meta:
        model=contractor 
        fields=('contractor_id','contractor_name','contractor_money','contractor_delete')

class designerSerializer(serializers.ModelSerializer):

    class Meta:
        model=designer 
        fields=('designer_id','designer_name','designer_money')

class accountSerializer(serializers.ModelSerializer):
    #builds = serializers.PrimaryKeyRelatedField(many=True, queryset=account.objects.all())
    class Meta:
        model=account 
        fields=('account_id','account_name','account_layout')


class bidSerializer(serializers.ModelSerializer):

    class Meta:
        model = bid
        fields = ('bid_id','bid_contractor_id','bid_build_id','bid_supply_id')
