import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render

def index(request):
    # response = requests.post('http://127.0.0.1:8000/api/DrugIntro/showDrugList/',json={"num":10,"start_id":1})
    # geodata = response.json()
    return render(request, 'frontpage.html')

# 對應各APP要自己新增
def Mgrsearchview(request):
    return render(request, 'Mgrsearchview.html')



def MgrsearchviewUpdatecase(request):
    return render(request, 'MgrsearchviewUpdatecase.html')

def MgrsearchviewAddcase(request):
    return render(request, 'MgrsearchviewAddcase.html')





