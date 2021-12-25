from rest_framework import serializers
from DrugNews.models import NewsList
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
class News(serializers.ModelSerializer):
  class Meta:
    model=NewsList
    fields='__all__'
@api_view(['GET','POST'])

def newsapi(request):
  if(request.method == 'GET'):
    # newsall=NewsList.objects.order_by("-id")[:10]
    newsall=NewsList.objects.order_by("-id")  # 211214-001 修改為回傳資料庫所有的新聞，由前端自行分頁
    serializer = News(newsall, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer=News(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['PUT','DELETE'])
def newsid(request, pk):
  try:
    new=NewsList.objects.get(pk=pk)
  except NewsList.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  if request.method == 'PUT':
    serializer = News(new, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    new.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# 211224-001 新增爬蟲抓取新聞標題、連結，並寫入資料庫
from DrugNews import models
from django.http import JsonResponse
@api_view(['POST'])
def autoUpdateNews(request):
  try:
    models.autoUpdate()
    return JsonResponse({"success":True, "desc":""},safe=False,status=status.HTTP_200_OK)
  except Exception as e:
    print(e)
    return JsonResponse({"success": False, "desc": str(e)}, safe=False,status=status.HTTP_400_BAD_REQUEST)
