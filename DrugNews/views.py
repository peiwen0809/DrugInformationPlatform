from django.http import HttpResponse
from django.shortcuts import render
import requests
import datetime
from dateutil.relativedelta import relativedelta
from DrugNews.models import NewsList as new
def index(request):
  return render(None, 'Drug/index.html')
def test(request):
  return render(None, 'Drug/test.html')
def hello(request):
  return HttpResponse('hello')
def get_news(request):
  

  onedate=datetime.date.today()- relativedelta(months=1)
  url = (f'https://newsapi.org/v2/everything?q=cocaine&from={onedate}&sortBy=popularity&apiKey=787457223f8e41c0ad544876961457ee')

  response = requests.get(url).json()['articles']
  for i in range(10):
    n=new(title=response[i]['title'],link=response[i]['url'])
    n.save()
  return HttpResponse('successful')

def Mgrnewsview(request):
    return render(request, 'Mgrnewsview.html')


def Newsview(request):
  return render(request, 'Newsview.html')