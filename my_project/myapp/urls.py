from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [

    url(r'^user/', views.UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)$',views.UserDetail.as_view()),
    url(r'^supplyInfo/',views.get_all_supplyinfo.as_view()),
    url(r'^account/',views.AccountList.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)