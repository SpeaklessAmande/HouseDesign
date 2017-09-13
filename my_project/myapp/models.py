from django.db import models

# Create your models here.
# coding:utf-8
from django.db import models
import django.utils.timezone as timezone
import datetime

#状态删除位的结构
deleteState = (
    (u'dele','已删除'),
    (u'no','正常'),
)

#承包商表
class constractor(models.Model):
    constractor_id=models.AutoField(primary_key=True,verbose_name='承包商ID')
    constractor_name=models.CharField(max_length=20,default='',verbose_name='承包商名称')
    constractor_price=models.IntegerField(null=True,verbose_name='承包商工费')
    constractor_money=models.IntegerField(null=True,verbose_name='承包商花销')
    constractor_delete=models.CharField(max_length=4,choices=deleteState,default='正常',verbose_name='承包商删除位')

    def __str__(self):
            return str(self.constractor_id)

    class Meta:
        verbose_name = '承包商'
        verbose_name_plural = '承包商'

#供应商表
class supply(models.Model):
    supply_id=models.AutoField(primary_key=True, verbose_name='供应商ID')
    supply_light=models.IntegerField(null=True,verbose_name='灯具单价')
    supply_tel=models.IntegerField(null=True,verbose_name='联系方式')
    supply_furniture=models.IntegerField(null=True,verbose_name='家具单价')
    supply_wood=models.IntegerField(null=True,verbose_name='木材单价')
    supply_floor=models.IntegerField(null=True,verbose_name='地板单价')
    supply_name=models.CharField(max_length=20,default='',verbose_name='供应商名字')
    supply_delete=models.CharField(max_length=10,choices=deleteState,default='正常',verbose_name='删除状态位')

    def __str__(self):
            return str(self.supply_id)
    class Meta:
        verbose_name = '供应商'
        verbose_name_plural = '供应商'


class designer(models.Model):
    designer_id = models.AutoField(primary_key=True,verbose_name='设计师id')
    designer_name = models.CharField(max_length=20,verbose_name='设计师姓名')
    designer_money = models.IntegerField(verbose_name='总花销')

    def __str__(self):
        return str(self.designer_id)
    class Meta:
        verbose_name = '设计师'
        verbose_name_plural = '设计人员'


#账户表
class account(models.Model):
    account_id=models.AutoField(primary_key=True,verbose_name='账户ID')
    account_name=models.CharField(max_length=20,default='',verbose_name='用户名')
    account_layout=models.IntegerField(null=True,verbose_name='总花销')

    def __str__(self):
            return str(self.account_id)
    class Meta:
        verbose_name = '账户'
        verbose_name_plural = '账户'


#订单表
class build(models.Model):
    build_id = models.AutoField(primary_key=True,verbose_name='主键')
    build_name = models.CharField(max_length=20,verbose_name='订单名')
    build_account_id = models.ForeignKey(account,related_name='buildAccount')
    build_designer = models.ForeignKey(designer,related_name='buildDesignerId')
    build_blueprint = models.CharField(max_length=255,null=True,verbose_name='蓝图')
    build_blueprint_price = models.IntegerField(verbose_name='设计费')
    build_date = models.DateTimeField(auto_now_add=True,verbose_name='记录创建时间')
    build_wood = models.IntegerField(null=True,verbose_name='木材估量')
    build_light = models.IntegerField(null=True,verbose_name='灯具估量')
    build_floor = models.IntegerField(null=True,verbose_name='地板估量')
    build_furniture = models.IntegerField(null=True,verbose_name='家具估量')
    build_supply = models.ForeignKey(supply,related_name='buildSupplyId',null=True)
    build_contractor = models.ForeignKey(constractor,related_name='buildContractorId',null=True)
    build_delete_status = models.CharField(max_length=4,choices=deleteState,default='正常',verbose_name='删除')
    
    def __str__(self):
        return str(self.build_account_id)
    
    class Meta:
        verbose_name = '订单表'
        verbose_name_plural = '订单表项'

#log表
class log(models.Model):
    log_id = models.IntegerField(primary_key=True,verbose_name='日志id')
    log_build_id =models.ForeignKey(build,null=True,related_name='buildId')
    log_tender = models.DateTimeField(verbose_name='招标节点')
    log_construction = models.DateTimeField(verbose_name='施工时间节点')
    log_accept = models.DateTimeField(verbose_name='验收时间节点')
    def __str__(self):
        return str(self.log_id)

    class Meta:
        verbose_name = 'log'
        verbose_name_plural = 'log表'


#用户表
class user(models.Model):
    user_id = models.AutoField(primary_key=True,verbose_name='用户主键')
    user_pas = models.CharField(max_length=20,verbose_name='密码')
    user_tel = models.CharField(max_length=11,verbose_name='电话')
    user_account_id = models.ForeignKey(account,related_name='userAccountId',null=True)
    user_designer_id = models.ForeignKey(designer,related_name='userDesignerId',null=True)
    user_contractor_id = models.ForeignKey(constractor,related_name='userConstractorId',null=True)

    def __str__(self):
            return self.user_tel
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户表'

#评论表
class comment(models.Model):
    comment_id = models.AutoField(primary_key=True,verbose_name='评论id')
    comment_content = models.CharField(max_length=255,verbose_name='内容')
    comment_time = models.DateTimeField(verbose_name='评论时间')
    comment_build_id = models.ForeignKey(build,related_name='commentBuildId')
    comment_user_id = models.ForeignKey(user,related_name='commentUserId')

    def __str__(self):
            return str(self.comment_id)
    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'

#竞标
class bid(models.Model):
    bid_id = models.AutoField(primary_key=True,verbose_name='竞标id')
    bid_contractor_id = models.ForeignKey(constractor,related_name='bidContractorId')
    bid_build_id = models.ForeignKey(build,related_name='bidBuildId')

    def __str__(self):
        return str(self.bid_id)

    class Meta:
        verbose_name = '竞标'
        verbose_name_plural = '竞标'