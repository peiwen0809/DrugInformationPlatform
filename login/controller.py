from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action

from login.serializers import AdminSerializer
from login.models import Admin

from django.http import HttpResponse, JsonResponse, request
from . import models


# Create your views here.


class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

    # http://127.0.0.1:8000/api/login/login
    # {"account":"admin","password":"admin123"}
    # {"success":True/False, "desc":"帳號/密碼錯誤"}
    @action(detail=False, methods=['post'])
    def login(self, request):
        account = request.data['account']
        password = request.data['password']
        if account.strip() and password:  # 確保使用者名稱和密碼都不為空
            try:
                user = models.Admin.objects.get(account=account)
            except:
                # 使用者不存在
                return JsonResponse({"success": False, "desc": "Account does not exist"})

            if user.password == password:
                return JsonResponse({"success": True, "desc": "Successful"})
            else:
                # 密碼不正確
                return JsonResponse({"success": False, "desc": "Incorrect password"})
        else:
            return JsonResponse({"success": False, "desc": "Error"})

