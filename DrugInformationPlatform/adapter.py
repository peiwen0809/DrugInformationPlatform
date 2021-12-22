import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render

def index(request):
    # response = requests.post('http://127.0.0.1:8000/api/DrugIntro/showDrugList/',json={"num":10,"start_id":1})
    # geodata = response.json()
    return render(request, 'frontpage.html')





