from rest_framework.authentication import SessionAuthentication
from .models import *

class DisableCSRF(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
#django 1.8版本前上面生效
#django 1.10之后下面有效
#我是django 1.11

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def has_permission(self, request, view):
       
        return  True
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening