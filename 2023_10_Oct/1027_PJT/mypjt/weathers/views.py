from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests

from django.conf import settings
from .serializers import WeatherSerializer

from django.http import JsonResponse
from .models import Weather
# Create your views here.

@api_view(['GET'])
def index(request):
    api_key = settings.API_KEY
    city = 'Seoul,KR'
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
    
    response = requests.get(url).json()
    
    return Response(response)

@api_view(['GET'])
def save_data(request):
    api_key = settings.API_KEY
    city = 'Seoul,KR'
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}' 
    response = requests.get(url).json()
    
    for li in response.get('list'):
        Save_data = {
            'dt_txt' : li.get('dt_txt'),
            'temp' : li.get('main').get('temp'),
            'feels_like' : li.get('main').get('feels_like'),
        }
        # 반복하며 포장,저장
        # 저장하기 위해 데이터를 포장
        serializer = WeatherSerializer(data=Save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
    # 저장완료 메시지를 반환하고 싶습니다. import -> f
    return JsonResponse({'message' : 'okay'})

# DB에 저장된  전체 데이터를 조회 할 것.
@api_view(['GET'])
def list_data(request):
    weathers = Weather.objects.all() # 얘는 데이터가 아님 // 쿼리셋임
    
    # JSON으로 포장합시다.
    serializer = WeatherSerializer(weathers, many=True) 
    # improve query 
    return Response(serializer.data)


@api_view(['GET'])
def hot_weathers(request):
    # 특정 조건을 걸어서 반환하자
    # 1. 데이터를 필터링 > 필터링 된 것을 모두 포장
    # 2. Serializer 자체 필터링
    # 이번에는 거르고 포장하는 것이 맞다.
    weathers = Weather.objects.all()
    hot_weathers = []
    for weather in weathers: 
        # 쿼리셋 반복이기에, . 으로 접근 가능하다.
        # 섭씨 : K - 273.15
        temp = round(weather.temp - 273.15, 2)
        if temp > 10:
            hot_weathers.append(weather)
        serializer = WeatherSerializer(hot_weathers, many=True)
        return Response(serializer.data)
# 비어있는 리스트가 나온다???? -> 오히려 좋아


