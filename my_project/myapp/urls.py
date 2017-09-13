from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [

    url(r'^user/', views.UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)$',views.UserDetail.as_view()),
    url(r'^supplyInfo/',views.get_all_supplyinfo.as_view()),
    url(r'^supplyInfo/(?P<pk>[0-9]+)$',views.get_one_supplyinfo.as_view()),
    url(r'^userCost/(?P<pk>[0-9]+)$',views.get_bill),
    url(r'^account/',views.AccountList.as_view()),
    url(r'^login/$',views.login),
    url(r'^blueprint/$',views.blueprint_first),
    url(r'^comment/$',views.addComment),
    url(r'^bid/$',views.addBid),
    url(r'^confirm/$',views.confirmNode),
]
urlpatterns = format_suffix_patterns(urlpatterns)