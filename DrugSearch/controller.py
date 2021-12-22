from django.http import JsonResponse

from DrugSearch.models import *
from DrugSearch.serializers import *

from rest_framework import viewsets
from rest_framework.decorators import action
import matplotlib.pyplot as plt

# Create your views here.
# 類似Controller的功能，接收前端request
class DrugSearchViewSet(viewsets.ModelViewSet):
    # queryset = DrugCountry.objects.all()
    # serializer_class = DrugCountrySerializer

    imgUrl = 'StatisticsIMG/'  # 圖片儲存路徑，修改成相對路徑
    plt.figure(figsize=(12, 6))  # 設定畫布的尺寸

    # 畫圖
    def drawPlot(self, imgName, legendArr=[]):
        if legendArr:
            plt.legend(legendArr, bbox_to_anchor=(1.0, 1.0))  # 圖例說明，指定圖例位置在圖表外
        # 設定字體以顯示中文
        plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
        plt.rcParams['axes.unicode_minus'] = False
        # 加座標軸文字
        plt.xlabel("年")
        plt.ylabel("人數")
        plt.tight_layout()  # 避免座標軸文字被裁切
        # 另存圖片，如果要存的話要再show前。否則圖片會是空白
        plt.savefig(self.imgUrl + imgName)
        plt.clf()  # 清除當前圖形
        # plt.show()


    # /DIP/DrugIntro/getCountryYearNum/
    # 取得一個國家每年的吸毒人數
    @action(detail=False, methods=['post'])
    def getCountryYearNum(self, request):
        #{"id":1}
        country_id = request.data['id']
        countryYearNum = DrugCountry.countryYearNum(country_id=country_id)
        serializer = DrugCountrySerializer(countryYearNum, many=True)  # many=true means queryset 包含多個項目（項目列表）
        if len(serializer.data) == 0:  #TODO 錯誤訊息的格式
            return JsonResponse({"sucecss":False,"desc":"No drug found"})
        # print(serializer.data)
        #取出年份、人數的陣列
        yearArr = []
        numArr = []
        response = []  # 211210-001 修改為回傳實際資料，由前端畫圖
        for d in serializer.data:
            yearArr.append(str(d['year']))
            numArr.append(d['num'])

            # 211210-001 修改為回傳實際資料，由前端畫圖
            num_of_people = {"year":str(d['year']),"num":d['num']}
            response.append(num_of_people)

        # 畫圖
        # 211213-001 畫圖會影響效能 mark
        # plt.plot(yearArr, numArr, 'r')
        # imgName = "country_year_num.png"
        # self.drawPlot(imgName)

        # return JsonResponse({'id':country_id,'img':self.imgUrl + imgName}, safe=False)  # 回傳圖片路徑
        return JsonResponse({'data':response}, safe=False)  # 211210-001 修改為回傳實際資料，由前端畫圖
        # return JsonResponse(serializer.data,safe=False)  # 為了允許非 dict 對像被序列化，將安全參數設置為 False

    # /DIP/DrugIntro/getAgeNum/
    # 取得一個國家每年的吸毒人數，依年齡層區分
    @action(detail=False, methods=['post'])
    def getAgeNum(self, request):
        # {"id":1}
        country_id = request.data['id']
        ageNum = DrugAge.ageNum(country_id=country_id)

        # 211210-001 修改為回傳實際資料，由前端畫圖
        response = []
        for r in ageNum:
            num_of_people = {"year": str(r.year), "num": r.num, "age": r.age_range,"age_id":r.age_id}
            response.append(num_of_people)

        # 211213-001 畫圖會影響效能 mark ==============start=================
        '''
        ageSet = {}  # 各年齡層人數 {"0-19":{"num":[123,456],"year":[2019,2020]},"20-29":{"num":[123,456],"year":[2019,2020]},...}
        # 將結果取出，存放到特定物件
        for r in ageNum:
            if r.age_range in ageSet.keys():  # 如果這個年齡層已經有資料了，將資料加入原本的array
                tmp = ageSet.get(r.age_range)  # 取出毒品種類的人數及年份
                numTmp = tmp.get("num")  # 取出人數
                numTmp.append(r.num)
                yearTmp = tmp.get("year")  # 取出年份
                yearTmp.append(str(r.year))
                ageSet[r.age_range] = {"num":numTmp,"year":yearTmp}
            else:
                ageSet[r.age_range] = {"num":[r.num],"year":[str(r.year)]}
        # serializer = DrugAgeSerializer(ageNum, many=True)  # many=true means queryset 包含多個項目（項目列表）
        # if len(serializer.data) == 0:  # TODO 錯誤訊息的格式
        #     return JsonResponse({"sucecss": False, "desc": "No drug found"})

        
        # 畫圖
        # for key in ageSet:
        #     plt.plot(ageSet[key].get("year"), ageSet[key].get("num"))
        # imgName = "age_num.png"
        # self.drawPlot(imgName, ageSet.keys())
        return JsonResponse({'id': country_id, 'img': self.imgUrl + imgName},
                            safe=False)  # 回傳圖片路徑
        '''
        # 211213-001 ==================end===========================
        return JsonResponse({"data": response}, safe=False)  # 211210-001 修改為回傳實際資料，由前端畫圖
        # return JsonResponse(serializer.data,safe=False)  # 為了允許非 dict 對像被序列化，將安全參數設置為 False


    # /DIP/DrugIntro/getGenderNum/
    # 取得一個國家每年的吸毒人數，依性別區分
    @action(detail=False, methods=['post'])
    def getGenderNum(self, request):
        # {"id":1}
        country_id = request.data['id']
        genderNum = DrugGender.genderNum(country_id=country_id)
        # serializer = DrugGenderSerializer(genderNum, many=True)  # many=true means queryset 包含多個項目（項目列表）
        # if len(serializer.data) == 0:  # TODO 錯誤訊息的格式
        #     return JsonResponse({"sucecss": False, "desc": "No drug found"})

        # 211210-001 修改為回傳實際資料，由前端畫圖
        response = []
        for r in genderNum:
            num_of_people = {"year": str(r.year), "num": r.num, "gender": r.gender, "gender_id": r.gender_id}
            response.append(num_of_people)

        # 211213-001 畫圖會影響效能 mark  ============start==============================
        '''
        genderSet = {}  # 各性別人數 {"男":{"num":[123,456],"year":[2019,2020]},"女":{"num":[123,456],"year":[2019,2020]}}
        # 將結果取出，存放到特定物件
        for r in genderNum:
            if r.gender in genderSet.keys():  # 如果這個性別已經有資料了，將資料加入原本的array
                tmp = genderSet.get(r.gender)  # 取出性別的人數及年份
                numTmp = tmp.get("num")  # 取出人數
                numTmp.append(r.num)
                yearTmp = tmp.get("year")  # 取出年份
                yearTmp.append(str(r.year))
                genderSet[r.gender] = {"num": numTmp, "year": yearTmp}
            else:
                genderSet[r.gender] = {"num": [r.num], "year": [str(r.year)]}
        # serializer = DrugAgeSerializer(ageNum, many=True)  # many=true means queryset 包含多個項目（項目列表）
        # if len(serializer.data) == 0:  # TODO 錯誤訊息的格式
        #     return JsonResponse({"sucecss": False, "desc": "No drug found"})
        
        # 畫圖
        for key in genderSet:
            plt.plot(genderSet[key].get("year"), genderSet[key].get("num"))
        # plt.legend(genderSet.keys())  # 圖例說明
        imgName = "gender_num.png"
        self.drawPlot(imgName, genderSet.keys())
        return JsonResponse({'id': country_id, 'img': self.imgUrl + imgName},
                            safe=False)  # 回傳圖片路徑
        '''
        # 211213-001 ===================end=======================
        return JsonResponse({"data": response}, safe=False)   # 211210-001 修改為回傳實際資料，由前端畫圖
        # return JsonResponse(serializer.data,safe=False)  # 為了允許非 dict 對像被序列化，將安全參數設置為 False


    # /DIP/DrugIntro/getDrugTypeNum/
    # 取得一個國家每年的吸毒人數，依毒品種類區分
    @action(detail=False, methods=['post'])
    def getDrugTypeNum(self, request):
        # {"id":1}
        country_id = request.data['id']
        drugTypeNum = DrugType.drugTypeNum(country_id=country_id)

        # 211210-001 修改為回傳實際資料，由前端畫圖
        response = []
        for r in drugTypeNum:
            num_of_people = {"year": str(r.year), "num": r.num, "type": r.ch_name, "type_id": r.drug_id}
            response.append(num_of_people)

        # 211213-001 畫圖會影響效能 mark ====================start======================
        '''
        drugTypeSet = {}  # 各毒品種類人數 {"大麻":{"num":[123,456],"year":[2019,2020]},"海洛因":{"num":[123,456],"year":[2019,2020]}}
        # 將結果取出，存放到特定物件
        for r in drugTypeNum:
            if r.ch_name in drugTypeSet.keys():  # 如果這個毒品種類已經有資料了，將資料加入原本的array
                tmp = drugTypeSet.get(r.ch_name)  # 取出毒品種類的人數及年份
                numTmp = tmp.get("num")  # 取出人數
                numTmp.append(r.num)
                yearTmp = tmp.get("year")  # 取出年份
                yearTmp.append(str(r.year))
                drugTypeSet[r.ch_name] = {"num":numTmp,"year":yearTmp}
            else:
                drugTypeSet[r.ch_name] = {"num":[r.num],"year":[str(r.year)]}
        # serializer = DrugAgeSerializer(ageNum, many=True)  # many=true means queryset 包含多個項目（項目列表）
        # if len(serializer.data) == 0:  # TODO 錯誤訊息的格式
        #     return JsonResponse({"sucecss": False, "desc": "No drug found"})

        # 畫圖
        # for key in drugTypeSet:
        #     plt.plot(drugTypeSet[key].get("year"), drugTypeSet[key].get("num"))
        # # plt.legend(drugTypeSet.keys())  # 圖例說明
        # imgName = "drug_type_num.png"
        # self.drawPlot(imgName, drugTypeSet.keys())
        # print(drugTypeSet)
        return JsonResponse({'id': country_id, 'img': self.imgUrl + imgName},
                            safe=False)  # 回傳圖片路徑
        '''
        # 211213-001 ===================end=======================
        return JsonResponse({"data": response}, safe=False)   # 211210-001 修改為回傳實際資料，由前端畫圖
        # return JsonResponse(serializer.data,safe=False)  # 為了允許非 dict 對像被序列化，將安全參數設置為 False