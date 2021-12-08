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
    newsall=NewsList.objects.order_by("-id")[:10]
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
