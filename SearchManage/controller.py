from django.http import JsonResponse

from SearchManage.models import *
from SearchManage.serializers import *

from rest_framework import viewsets
from rest_framework.decorators import action


# Create your views here.
# 類似Controller的功能，接收前端request
class SearchManageViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'getCountryYearNum' or self.action == 'insertCountryYearNum':
            return DrugCountrySerializer

        elif self.action == 'getAgeNum' or self.action == 'insertAgeNum':
            return DrugAgeSerializer

        elif self.action == 'getGenderNum' or self.action == 'insertGenderNum':
            return DrugGenderSerializer
        else:
            return DrugTypeSerializer

    # queryset = DrugCountry.objects.all()
    # serializer_class = DrugCountrySerializer

    # {"country_id": 1, "year": "2020", "num": 400000,
    # "data_age": [{"age_id": 1, "num": 20000}, {"age_id": 2, "num": 20000}, {...}],
    # "data_gender": [{"gender": "male", "num": 20000}, {"gender": "female", "num": 20000}],
    # "data_drug": [{"drug_id": 1, "num": 20000}, {"drug_id": 2, "num": 20000}, {...}]}
    # http://127.0.0.1:8000/api/SearchManage/getCU/
    """@action(detail=False, methods=['post'])
    def getCU(self, request):
        country_id = request.data['country_id']
        year = request.data['year']
        data_age = request.data['data_age']
        data_gender = request.data['data_gender']
        data_drug = request.data['data_drug']
        for a in data_age:
            age_id = a.data['age_id']
            num = a.data['num']
            ageNum = DrugAge.ageNum(age_id=age_id, country_id=country_id, year=year, num=num)

        for b in data_gender:
            gender = b.data['gender']
            num = b.data['num']
            genderNum = DrugGender.genderNum(gender=gender, country_id=country_id, year=year, num=num)

        for c in data_drug:
            drug_id = c.data['drug_id']
            num = c.data['num']
            drugNum = DrugType.drugTypeNum(drug_id=drug_id, country_id=country_id, year=year, num=num)
        """

    # http://127.0.0.1:8000/api/SearchManage/getCountryYearNum/
    # 改一個國家每年的吸毒人數
    # {"country_id": 1, "year": "2020", "num": 20000}
    # {"success": true / false, "desc": "錯誤原因"}
    @action(detail=False, methods=['post'])
    def getCountryYearNum(self, request):
        # {"country_id": 1, "year": "2020", "num": 20000}
        country_id = request.data['country_id']
        year = request.data['year']
        num = request.data['num']
        result = DrugCountry.countryYearNum(country_id=country_id, year=year, num=num)
        if result == True:
            return JsonResponse({"success": True, "desc": "Successful!"})
        elif result == False:
            return JsonResponse({"success": False, "desc": "Error"})
        else:
            return JsonResponse({"success": False, "desc": result})

    # http://127.0.0.1:8000/api/SearchManage/insertCountryYearNum/
    # 新增總人數
    @action(detail=False, methods=['post'])
    def insertCountryYearNum(self, request):
        country_id = request.data['country_id']
        year = request.data['year']
        num = request.data['num']
        result = DrugCountry.createCountryYearNum(country_id=country_id, year=year, num=num)
        if result == True:
            return JsonResponse({"success": True, "desc": "Successful!"})
        elif result == False:
            return JsonResponse({"success": False, "desc": "Error"})
        else:
            return JsonResponse({"success": False, "desc": result})

    # http://127.0.0.1:8000/api/SearchManage/getAgeNum/
    # 改一個國家每年的吸毒人數，依年齡層區分
    # {"country_id": 1, "year": "2020", "data": [{"age_id": 1, "num": 20000}, {"age_id": 2, "num": 20000}, {...}]}
    # {"success": true / false, "desc": "錯誤原因"}
    @action(detail=False, methods=['post'])
    def getAgeNum(self, request):
        country_id = request.data['country_id']
        year = request.data['year']
        data = request.data['data']
        for a in data:
            age_id = a['age_id']
            num = a['num']
            print(a)
            result = DrugAge.ageNum(country_id=country_id, year=year, num=num, age_id=age_id)
            print(result)
            if result == False:
                return JsonResponse({"success": False, "desc": "Error"})
            elif result == True:
                continue
            else:
                return JsonResponse({"success": False, "desc": result})
        return JsonResponse({"success": True, "desc": "Successful!"})

    # http://127.0.0.1:8000/api/SearchManage/insertAgeNum/
    # 新增年齡人數
    @action(detail=False, methods=['post'])
    def insertAgeNum(self, request):
        country_id = request.data['country_id']
        year = request.data['year']
        data = request.data['data']
        for a in data:
            age_id = a['age_id']
            num = a['num']
            result = DrugAge.createAgeNum(country_id=country_id, year=year, num=num, age_id=age_id)
            if result == False:
                return JsonResponse({"success": False, "desc": "Error"})
            elif result == True:
                continue
            else:
                return JsonResponse({"success": False, "desc": result})
        return JsonResponse({"success": True, "desc": "Successful!"})

    # http://127.0.0.1:8000/api/SearchManage/getGenderNum/
    # 改一個國家每年的吸毒人數，依性別區分
    # {"country_id": 1, "year": "2020", "data": [{"gender_id": "1", "num": 20000}, {"gender_id": "2", "num": 20000}]}
    # {"success": true / false, "desc": "錯誤原因"}
    @action(detail=False, methods=['post'])
    def getGenderNum(self, request):
        country_id = request.data['country_id']
        year = request.data['year']
        data = request.data['data']
        for b in data:
            gender_id = b['gender_id']
            num = b['num']
            result = DrugGender.genderNum(country_id=country_id, year=year, num=num, gender_id=gender_id)
            if result == False:
                return JsonResponse({"success": False, "desc": "Error"})
            elif result == True:
                continue
            else:
                return JsonResponse({"success": False, "desc": result})
        return JsonResponse({"success": True, "desc": "Successful!"})

    # http://127.0.0.1:8000/api/SearchManage/insertGenderNum/
    # 新增性別人數
    @action(detail=False, methods=['post'])
    def insertGenderNum(self, request):
        country_id = request.data['country_id']
        year = request.data['year']
        data = request.data['data']
        for b in data:
            gender_id = b['gender_id']
            num = b['num']
            result = DrugGender.createGenderNum(country_id=country_id, year=year, num=num, gender_id=gender_id)
            if result == False:
                return JsonResponse({"success": False, "desc": "Error"})
            elif result == True:
                continue
            else:
                return JsonResponse({"success": False, "desc": result})
        return JsonResponse({"success": True, "desc": "Successful!"})

    # http://127.0.0.1:8000/api/SearchManage/getDrugTypeNum/
    # 改一個國家每年的吸毒人數，依毒品種類區分
    # {"country_id": 1, "year": "2020", "data": [{"drug_id": 1, "num": 20000}, {"drug_id": 2, "num": 20000}, {...}]}
    # {"success": true / false, "desc": "錯誤原因"}
    @action(detail=False, methods=['post'])
    def getDrugTypeNum(self, request):
        country_id = request.data['country_id']
        year = request.data['year']
        data = request.data['data']
        for c in data:
            drug_id = c['drug_id']
            num = c['num']
            result = DrugType.drugTypeNum(country_id=country_id, year=year, num=num, drug_id=drug_id)
            if result == False:
                return JsonResponse({"success": False, "desc": "Error"})
            elif result == True:
                continue
            else:
                return JsonResponse({"success": False, "desc": result})
        return JsonResponse({"success": True, "desc": "Successful!"})

    # http://127.0.0.1:8000/api/SearchManage/insertDrugTypeNum/
    # 新增毒品人數
    @action(detail=False, methods=['post'])
    def insertDrugTypeNum(self, request):
        country_id = request.data['country_id']
        year = request.data['year']
        data = request.data['data']
        for c in data:
            drug_id = c['drug_id']
            num = c['num']
            result = DrugType.createDrugTypeNum(country_id=country_id, year=year, num=num, drug_id=drug_id)
            if result == False:
                return JsonResponse({"success": False, "desc": "Error"})
            elif result == True:
                continue
            else:
                return JsonResponse({"success": False, "desc": result})
        return JsonResponse({"success": True, "desc": "Successful!"})

    # 211226-001 新增刪除資料的API {"country_id:"0", "year":"2020}
    @action(detail=False, methods=['post'])
    def delCountryYearData(self, request):
        country_id = request.data['country_id']
        year = request.data['year']
        tableArr = ["country_year_num", "age_num", "gender_num", "drug_num"]
        for table in tableArr:
            result, desc = DelObject.delData(country_id=country_id, year=year, table=table)
            if not result:
                return JsonResponse({"success": result, "desc": desc}, safe=False)
        return JsonResponse({"success": True, "desc": ""}, safe=False)
