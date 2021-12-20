# Create your views here.

from django.http import HttpResponse, JsonResponse, request
from requests import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from BaseTableSearch.models import *
from BaseTableSearch.serializers import *

from rest_framework import viewsets, status
from rest_framework.decorators import api_view,action

# Create your views here.
class BaseTableSearchViewSet(viewsets.ModelViewSet):
    # queryset = AgeTableSearch.objects.all()
    # serializer_class = AgeTableSearchSerializer

    # /DIP/BaseTableSearch/getBaseTable/
    # 取得基礎資料表的內容
    @action(detail=False, methods=['post'])
    def getBaseTable(self, request):
        #{"table":1}
        table = request.data['table']
        searchModel = AgeTableSearch
        searchSerializer = AgeTableSearchSerializer
        if table == "gender":
            searchModel = GenderTableSearch
            searchSerializer = GenderTableSearchSerializer

        table_info = searchModel.getTable(table=table)
        serializer = searchSerializer(table_info, many=True)  # many=true means queryset 包含多個項目（項目列表
        if len(serializer.data) == 0:  #TODO 錯誤訊息的格式
            return JsonResponse({"sucecss":False,"desc":"No data"})
        return JsonResponse({"data": serializer.data},safe=False)  # 為了允許非 dict 對像被序列化，將安全參數設置為 False


