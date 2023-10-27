# 2023_10_27 

# API Server 제작
> 날씨 데이터를 활용한 REST API Server 구축
## Django!

# REST 

1. URL 식별자만 표시하자
2. HTTP Method 로 표기하자



사실 우리는 날씨정보가 없습니다.
우리는 날씨 정보 원본 데이터를 OpenWeatherMap API 를 통해 가져올 것입니다.   
![Alt text](image.png)
<br>
(클라이언트는 모를겁니다.)


응애 POST맨!!!!!!

# 참고 
백엔드 개발 vs 프론트엔드 개발
백 : REST API 서버 개발  
프론트엔드 개발  
REST API를 사용하여, 결과를 받아 화면 구성   
Django 백엔드 개발   
차후 Vue.js 학습 -> 프론트엔드 개발  
하나의 완성된 웹 App 개발  




api 뭔가 잘 합시다.

settings.py 에 필요한건 ? 

```py

# base dir 경로에
# .env 이렇게 만듦
# view 함수에서 api 제거.
# .gitignore > env 추가 필수

# settings에 많이 함.
# 내 PC 파일안에 저장된 API_KEY 변수를 가져온다
import environ
import os

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
# False if not in os.environ because of casting above
API_KEY = env('API_KEY')

# views.py // AUTH_USER_MODEL 같은 것
from django.conf import settings
```
띄어쓰기 하지 마쇼 

가져오기 전에 구조 파악하기
1. list
-  dt-txt
-  main
   -  temp
   -  feel-like
-  models.py gogo


Serializer : 포장
```py
weathers = Weather.objects.all() # 얘는 데이터가 아님 // 쿼리셋임
# 데이터가 아니므로, JSON으로 보내라고 하면  JSON serializerable 하지 않다.
# 그러니까
# JSON으로 포장합시다.
serializer = WeatherSerializer(weathers, many=True) 
return Respons(serializer.data)


# 예시
class WeatherSerailizer(serialzers.ModelSerializer):
  class Meta(상속받는Serializer.Meta):
    model = Weather
    ... 추가하고 싶은 것
    fields = 상속받는Serializer.Meta.fileds + ('new_filed',)
```


# 관통 버전 선택 하는 날!
각 프로젝트가 무슨 주제인가, 내용인지 알아야 하지 않곘음? 
> Final-pjt 기준으로 생각하려무나.
7,8,9 특) 배운 것 복습



# 추 천 알 고 리 즘
# 추 천 알 고 리 즘
# 추 천 알 고 리 즘
# 추 천 알 고 리 즘
# 추 천 알 고 리 즘
# 추 천 알 고 리 즘
# 추 천 알 고 리 즘
# 추 천 알 고 리 즘
# 추 천 알 고 리 즘
# 추 천 알 고 리 즘
# 추 천 알 고 리 즘
# 추 천 알 고 리 즘
# 추 천 알 고 리 즘
# 추 천 알 고 리 즘
어떤 트랙이든지 데이터만 다를 뿐,,,, 비슷,,,