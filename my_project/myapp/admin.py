from django.contrib import admin
from .models import *
# Register your models here.


class contractorAdmin(admin.ModelAdmin):
    list_display = ('contractor_id',)
    list_filter = ('contractor_name','contractor_price',)

class supplyAdmin(admin.ModelAdmin):
    list_display = ('supply_id',)
    list_filter = ()

class designerAdmin(admin.ModelAdmin):
    list_display = ('designer_id',)
    list_filter = ('designer_name',)


class accountAdmin(admin.ModelAdmin):
    list_display = ('account_id',)
    list_filter = ()

class buildAdmin(admin.ModelAdmin):
    list_display = ('build_id',)
    list_filter = ()

class logAdmin(admin.ModelAdmin):
    list_display = ('log_id',)
    list_filter = ()

class userAdmin(admin.ModelAdmin):
    list_display = ('user_id',)
    list_filter = ()

class commentAdmin(admin.ModelAdmin):
    list_display = ('comment_id',)
    list_filter = ()

class bidAdmin(admin.ModelAdmin):
    list_display = ('bid_id',)
    list_filter = ()


admin.site.register(contractor,contractorAdmin)
admin.site.register(supply,supplyAdmin)
admin.site.register(designer,designerAdmin)
admin.site.register(account,accountAdmin)
admin.site.register(build,buildAdmin)
admin.site.register(log,logAdmin)
admin.site.register(user,userAdmin)
admin.site.register(comment,commentAdmin)
admin.site.register(bid,bidAdmin)