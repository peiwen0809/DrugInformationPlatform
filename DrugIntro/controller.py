# Create your views here.

from django.http import HttpResponse, JsonResponse, request
from requests import Response
from rest_framework.renderers import JSONRenderer

from DrugIntro.models import DrugIntro
from DrugIntro.serializers import DrugIntroSerializer

from rest_framework import viewsets, status
from rest_framework.decorators import api_view,action

# Create your views here.
class DrugIntroViewSet(viewsets.ModelViewSet):
    queryset = DrugIntro.objects.all()
    serializer_class = DrugIntroSerializer

    # /DIP/DrugIntro/getDrugInfo/
    # 取得毒品詳細資訊
    @action(detail=False, methods=['post'])
    def getDrugInfo(self, request):
        #{"id":1}
        drug_id = request.data['id']
        drug_info = DrugIntro.drugInfo(id=drug_id)
        serializer = DrugIntroSerializer(drug_info, many=True)  # many=true means queryset 包含多個項目（項目列表）
        # {"id":1,"name":"大麻","eng_name":"marijuana","desc":"XXXXXX"}
        # 如果資料表欄位名稱跟response的名稱不相同，需要額外轉換
        # response = {
        #     'id':0,
        #     'name':'123',
        #     "eng_name":"",
        #     "desc":""
        # }
        # response["id"] = serializer.data[0]['id']
        # response["name"] = serializer.data[0]['drug_name']
        # response["eng_name"] = serializer.data[0]['drug_eng_name']
        # response["desc"] = serializer.data[0]['drug_desc']
        # print(response)
        # return HttpResponse(response, status.HTTP_200_OK)
        if len(serializer.data) == 0:  #TODO 錯誤訊息的格式
            return JsonResponse({"sucecss":False,"desc":"No drug found"})
        return JsonResponse(serializer.data[0],safe=False)  # 為了允許非 dict 對像被序列化，將安全參數設置為 False

    # /DIP/DrugIntro/showDrugList/
    # 取得毒品清單
    @action(detail=False, methods=['post'])
    def showDrugList(self, request):
        # {"num": 10, "start_id": 1}
        num = request.data['num']
        start_id = request.data['start_id']
        drug_info = DrugIntro.drugList(num=num,start_id=start_id)
        serializer = DrugIntroSerializer(drug_info, many=True)
        # {"data":[{"id":1,"name":"大麻","eng_name":"marijuana"},{"id":2,"name":"海洛因","eng_name":"Heroin"},...]}
        # 如果資料表欄位名稱跟response的名稱不相同，需要額外轉換
        # list = []
        # for d in serializer.data:
        #     response = {
        #         'id': 0,
        #         'name': '',
        #         "eng_name": "",
        #         "desc": ""
        #     }
        #     response["id"] = d['id']
        #     response["name"] = d['drug_name']
        #     response["eng_name"] = d['drug_eng_name']
        #     response["desc"] = d['drug_desc']
        #     list.append(d)

        data = {'data':serializer.data}
        return JsonResponse(data)

